from datetime import datetime

from odoo import models, fields, api
from odoo.exceptions import ValidationError

##one to many de consultas, sola 1 activa.

class Treatment(models.Model):
    _name = 'hospital.treatment'
    _description = 'Treatment Information'

    name = fields.Char(string='Treatment', required=True)
    date = fields.Date(string='Date', default=datetime.now())
    description = fields.Text(string='Description')
    doctor_id = fields.Many2one('hospital.doctor', string='Doctor', required=True)
    state = fields.Selection([('draft', 'Draft'), ('in_progress', 'In Progress'), ('done', 'Done')], string='State', default='draft')


