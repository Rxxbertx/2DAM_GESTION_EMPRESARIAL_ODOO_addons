from odoo import models, fields,api


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

    # Creamos una funcion que nos devuelva el nombre completo del doctor
    @api.depends('name', 'last_name')
    def _get_full_name(self):
        for doctor in self:
            doctor.full_name = doctor.name + ' ' + doctor.last_name


