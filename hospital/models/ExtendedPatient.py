from odoo import models, fields


class ExtendedPatient(models.Model):
    _name = 'hospital.extended.patient'
    _description = 'Extended Patient Information'
    _inherit = 'hospital.patient'

    social_security_number = fields.Char(string='Social Security Number')
