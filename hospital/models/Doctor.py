from odoo import models, fields


class Doctor(models.Model):
    _name = 'hospital.doctor'
    _description = 'Doctor Information'

    name = fields.Char(string='Name', required=True)
    last_name = fields.Char(string='Last Name', required=True)
    specialization = fields.Char(string='Specialization')
    work_schedule = fields.Char(string='Work Schedule')
    phone = fields.Char(string='Phone')
    email = fields.Char(string='Email')
    treated_patients_ids = fields.Many2many('hospital.patient', string='Treated Patients')
