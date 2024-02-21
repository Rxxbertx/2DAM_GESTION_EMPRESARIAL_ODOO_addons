from odoo import models, fields, api
from odoo.exceptions import ValidationError


class Doctor(models.Model):
    _name = 'hospital.doctor'
    _description = 'Doctor Information'

    _inherit = 'hospital.person'

    specialization = fields.Char(string='Specialization')
    work_schedule = fields.Float(string='Hours of Work')
    email = fields.Char(string='Email', required=True)
    treated_patients_ids = fields.Many2many('hospital.admission', string='Treated Patients')
    patients = fields.One2many('hospital.admission', 'doctor_id', string='Patients')

    @api.constrains('patients')
    def get_three_patients(self):
        for doctor in self:
            if len(doctor.patients) > 3:
                doctor.patients = doctor.patients[:3]
                raise ValidationError("A doctor can only treat up to 3 patients at a time.")
