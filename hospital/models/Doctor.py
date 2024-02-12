from odoo import models, fields, api
from odoo.exceptions import ValidationError


class Doctor(models.Model):
    _name = 'hospital.doctor'
    _description = 'Doctor Information'

    name = fields.Char(string='Name', required=True)
    last_name = fields.Char(string='Last Name', required=True)
    specialization = fields.Char(string='Specialization')
    work_schedule = fields.Char(string='Hours of Work')
    phone = fields.Char(string='Phone', required=True)
    email = fields.Char(string='Email', required=True)
    treated_patients_ids = fields.Many2many('hospital.extended.patient', string='Treated Patients')
    full_name = fields.Char(string='Full Name', compute='_get_full_name', store=True)
    patients = fields.One2many('hospital.extended.patient', 'doctor_id', string='Patients')

    # Creamos una funcion que nos devuelva el nombre completo del doctor
    @api.depends('name', 'last_name')
    def _get_full_name(self):
        for doctor in self:
            doctor.full_name = doctor.name + ' ' + doctor.last_name

    @api.constrains('patients')
    def get_three_patients(self):
        for doctor in self:
            if len(doctor.patients) > 3:
                doctor.patients = doctor.patients[:3]
                raise ValidationError("A doctor can only treat up to 3 patients at a time.")
