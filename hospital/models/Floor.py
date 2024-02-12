from odoo import models, fields, api


class Floor(models.Model):
    _name = 'hospital.floor'
    _description = 'Floor Information'

    name = fields.Char(string='Floor Name', required=True)
    available_beds = fields.Integer(string='Available Beds', compute='_compute_available_beds')
    beds_ids = fields.One2many('hospital.bed', 'floor_id', string='Beds')

    total_beds = fields.Integer(string='Total Beds', compute='_compute_total_beds')
    occupied_beds = fields.Integer(string='Occupied Beds', compute='_compute_occupied_beds')

    @api.depends('beds_ids')
    def _compute_total_beds(self):
        for record in self:
            record.total_beds = len(record.beds_ids)

    @api.depends('beds_ids.state')
    def _compute_occupied_beds(self):
        for record in self:
            record.occupied_beds = len(record.beds_ids.filtered(lambda bed: bed.state == 'occupied'))

    @api.depends('beds_ids.state')
    def _compute_available_beds(self):
        for record in self:
            record.available_beds = len(record.beds_ids.filtered(lambda bed: bed.state == 'available'))
