from datetime import datetime

from odoo import models, fields


class Diagnosis(models.Model):
    _name = 'hospital.diagnosis'
    _description = 'Diagnosis Information'

    name = fields.Char(string='Diagnosis', required=True)
    date = fields.Date(string='Date', default=datetime.now())
    description = fields.Text(string='Description')
