from odoo import models, fields


class Bed(models.Model):
    _name = 'hospital.bed'
    _description = 'Bed Information'

    name = fields.Char(string='Bed Name', required=True)
    floor_id = fields.Many2one('hospital.floor', string='Floor')
    state = fields.Selection([('occupied', 'Occupied'), ('available', 'Available')], string='State')
    type = fields.Selection([('normal', 'Normal'), ('intensive_care', 'Intensive Care'), ('pediatric', 'Pediatric')],
                            string='Bed Type')
    patient_id = fields.One2many('hospital.extended.patient', 'bed_id', string='Patient')

# aplicar restricciones de integridad, por ejemplo que el nombre de la cama sea único en el sistema
