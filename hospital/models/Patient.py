from datetime import datetime

from odoo import models, fields, api
from odoo.exceptions import ValidationError


class Patient(models.Model):
    _name = 'hospital.patient'
    _description = 'Patient Information'

    _inherit = 'hospital.person'

    address = fields.Text(string='Address')
    allergies = fields.Text(string='Allergies')
    preexisting_conditions = fields.Text(string='Preexisting Conditions')
    state = fields.Selection([
        ('admitted', 'Admitted'),
        ('not_admitted', 'Not Admitted'),
    ], string='State', default='not_admitted')
    bed_id = fields.Many2one('hospital.bed', string='Bed', domain="[('state', '=', 'available')]")
    doctor_id = fields.Many2one('hospital.doctor', string='Doctor')
    social_security_number = fields.Char(string='Social Security Number')
    previous_bed = fields.Many2one('hospital.bed', string='Previous Bed')
    previous_doctor = fields.Many2one('hospital.doctor', string='Previous Doctor')

    # Creamos una condicion para que el numero de seguro social sea unico
    _sql_constraints = [
        ('social_security_number_unique',
         'UNIQUE(social_security_number)',
         'The Social Security Number must be unique.')
    ]

    @api.constrains('bed_id')
    def check_bed_availability(self):
        for record in self:
            if record.bed_id and record.bed_id.state == 'occupied':
                raise ValidationError("The bed is already occupied.")

    def write(self, vals):

        # Cambiar el estado de la cama anterior a 'available'

        res = super(Patient, self).write(vals)

        if 'bed_id' in vals:
            self.bed_id.state = 'occupied' if vals['bed_id'] else 'available'

        if self.bed_id and self.previous_bed != self.bed_id:
            self.previous_bed = self.bed_id

        if self.doctor_id and self.previous_doctor != self.doctor_id:
            self.previous_doctor = self.doctor_id

        if self.previous_bed and self.previous_bed != self.bed_id:
            self.previous_bed.state = 'available'

        if 'doctor_id' in vals:
            if self.doctor_id:
                self.state = 'admitted' if vals['doctor_id'] else 'not_admitted'

        if 'state' in vals:
            if vals['state'] == 'admitted':
                self.env['hospital.admission.history'].create({
                    'patient_id': self.id,
                    'admission_date': datetime.now(),
                })
            elif vals['state'] == 'not_admitted':
                admission_history = self.env['hospital.admission.history'].search([
                    ('patient_id.id', '=', self.id),
                ], order='admission_date desc', limit=1)
                if admission_history:
                    admission_history.write({
                        'discharge_date': datetime.now(),
                        'previous_bed': self.previous_bed.id,
                        'previous_doctor': self.previous_doctor.id,

                    })
        return res

    def discharge(self):
        if self.bed_id:
            self.bed_id.state = 'available'
            self.previous_bed = self.bed_id  # guarda la cama actual en previous_bed antes de dar de alta al paciente
            self.bed_id = False
        if self.doctor_id:
            self.previous_doctor = self.doctor_id
            self.doctor_id.treated_patients_ids += self
            self.doctor_id = False
        self.state = 'not_admitted'
