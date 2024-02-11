from odoo import models, fields, api
from odoo.exceptions import ValidationError


class Bed(models.Model):
    _name = 'hospital.bed'
    _description = 'Bed Information'

    name = fields.Char(string='Bed Name', required=True)
    floor_id = fields.Many2one('hospital.floor', string='Floor')
    state = fields.Selection([('occupied', 'Occupied'), ('available', 'Available')], string='State')
    type = fields.Selection([('normal', 'Normal'), ('intensive_care', 'Intensive Care'), ('pediatric', 'Pediatric')],
                            string='Bed Type')

    @api.constrains('state')
    def _check_state(self):
        for bed in self:
            if bed.state == 'occupied':
                raise ValidationError("Bed is occupied")
