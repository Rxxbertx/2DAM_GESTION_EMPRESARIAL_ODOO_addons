from odoo import models, fields, api
from odoo.exceptions import ValidationError


class Person(models.AbstractModel):
    _name = 'hospital.person'
    _description = 'Person Information'

    name = fields.Char(string='Name', required=True)
    last_name = fields.Char(string='Last Name', required=True)
    full_name = fields.Char(string='Full Name', compute='_get_full_name', store=True)
    date_of_birth = fields.Date(string='Date of Birth')
    gender = fields.Selection([('male', 'Male'), ('female', 'Female'), ('other', 'Other')], string='Gender')
    age = fields.Integer(string='Age', compute='_get_age', store=True)
    phone = fields.Char(string='Phone')

    @api.depends('name', 'last_name')
    def _get_full_name(self):
        for patient in self:
            patient.full_name = patient.name + ' ' + patient.last_name

    @api.depends('date_of_birth')
    def _get_age(self):
        for patient in self:
            if patient.date_of_birth:
                today = fields.Date.today()
                dob = fields.Datetime.from_string(patient.date_of_birth)
                age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
                patient.age = age
