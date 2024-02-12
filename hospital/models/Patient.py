from odoo import models, fields, api
from odoo.exceptions import ValidationError


class Patient(models.Model):
    _name = 'hospital.patient'
    _description = 'Patient Information'

    name = fields.Char(string='Name', required=True)
    last_name = fields.Char(string='Last Name', required=True)
    date_of_birth = fields.Date(string='Date of Birth')
    gender = fields.Selection([('male', 'Male'), ('female', 'Female'), ('other', 'Other')], string='Gender')
    address = fields.Text(string='Address')
    phone = fields.Char(string='Phone')
    allergies = fields.Text(string='Allergies')
    preexisting_conditions = fields.Text(string='Preexisting Conditions')
    state = fields.Selection([
        ('admitted', 'Admitted'),
        ('not_admitted', 'Not Admitted'),
    ], string='State', default='not_admitted')
    bed_id = fields.Many2one('hospital.bed', string='Bed', domain="[('state', '=', 'available')]")
    doctor_id = fields.Many2one('hospital.doctor', string='Doctor')

    @api.constrains('bed_id')
    def check_bed_availability(self):
        for record in self:
            if record.bed_id and record.bed_id.state == 'occupied':
                raise ValidationError("The bed is already occupied.")

    def write(self, vals):
        res = super(Patient, self).write(vals)
        if 'bed_id' in vals:
            self.bed_id.state = 'occupied' if vals['bed_id'] else 'available'
            self.state = 'admitted' if vals['bed_id'] else 'not_admitted'
    
        return res

    def discharge(self):
        self.bed_id.state = 'available'
        self.bed_id = False
        self.state = 'not_admitted'
