# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Ability(models.Model):
    _name = 'pokemon.abilities'
    _description = "Habilidades de pokemones"

    name = fields.Char(string="Nombre de la Habilidad", required=True)
    