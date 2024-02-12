from odoo import models, fields


class ExtendedPatient(models.Model):
    _name = 'hospital.extended.patient'
    _description = 'Extended Patient Information'
    _inherit = 'hospital.patient'

    social_security_number = fields.Char(string='Social Security Number')

    # Creamos una condicion para que el numero de seguro social sea unico
    _sql_constraints = [
        ('social_security_number_unique',
         'UNIQUE(social_security_number)',
         'The Social Security Number must be unique.')
    ]
