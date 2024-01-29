# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Abilities(models.Model):
    _name = 'pokemon.abilities'
    _description = "Habilidades de pokemones"

    name = fields.Char(string="Habilidad", required =True)
    