from encodings import utf_8


coding: utf_8

from odoo import models, fields, api
    
class Modelo(models.Model):
     _name = 'taller.modelo'
     _description='taller.modelo'
     
     name = fields.Char('Nombre', required=True)
     marca= fields.Many2one(string="Marca",comodel_name="taller.marca",required=True)

    