from odoo import models, fields,api


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

    # Creamos una funcion que nos devuelva el nombre completo del paciente
    @api.depends('name', 'last_name')
    def _get_full_name(self):
        for patient in self:
            patient.full_name = patient.name + ' ' + patient.last_name

    # Creamos una funcion que nos devuelva la edad del paciente
    @api.depends('date_of_birth')
    def _get_age(self):
        for patient in self:
            if patient.date_of_birth:
                today = fields.Date.today()
                dob = fields.Datetime.from_string(patient.date_of_birth)
                age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
                patient.age = age
