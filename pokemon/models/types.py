# -*- coding: utf-8 -*-
#!pip install pandas

from odoo import models, fields




class Types(models.Model):
    _name = 'pokemon.types'
    _description = 'Tipos de los pokemones'

    name = fields.Char(string = "Tipos", required = True)
    img = fields.Image(string="Logo")
    

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100