# -*- coding: utf-8 -*-
#!pip install pandas

from odoo import models, fields




class PType(models.Model):
    _name = 'pokemon.type'
    _description = 'Tipos de los pokemones'

    name = fields.Char(string = "Tipos", required = True)