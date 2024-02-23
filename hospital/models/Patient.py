from odoo import models, fields


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

    social_security_number = fields.Char(string='Social Security Number')

    admission_ids = fields.One2many('hospital.admission', 'patient_id', string='Admissions')

    # Creamos una condicion para que el numero de seguro social sea unico
    _sql_constraints = [
        ('social_security_number_unique',
         'UNIQUE(social_security_number)',
         'The Social Security Number must be unique.')
    ]
