from datetime import datetime

from odoo import models, fields


class Treatment(models.Model):
    _name = 'hospital.treatment'
    _description = 'Treatment Information'

    name = fields.Char(string='Treatment', required=True)
    date = fields.Date(string='Date', default=datetime.now())
    description = fields.Text(string='Description')
