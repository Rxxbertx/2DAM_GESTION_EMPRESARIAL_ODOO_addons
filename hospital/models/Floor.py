from odoo import models, fields


class Floor(models.Model):
    _name = 'hospital.floor'
    _description = 'Floor Information'

    name = fields.Char(string='Floor Name', required=True)
    total_beds = fields.Integer(string='Total Beds')
    occupied_beds = fields.Integer(string='Occupied Beds')
    available_beds = fields.Integer(string='Available Beds')
    beds_ids = fields.One2many('hospital.bed', 'floor_id', string='Beds')
