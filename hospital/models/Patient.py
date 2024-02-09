from odoo import models, fields


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
