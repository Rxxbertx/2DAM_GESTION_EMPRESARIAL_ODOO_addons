from encodings import utf_8


coding: utf_8

from odoo import models, fields, api


class Marca(models.Model):
    
    _name = 'taller.marca'
    _description = 'Creacion de marcas'

    name = fields.Char(srting = "Nombre",required=True)
    image = fields.Image(string='Imagen',widget="image")
    description = fields.Text(string = "Descripcion")