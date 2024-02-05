from odoo import models, fields, api

class Trainer(models.Model):
    _name = 'pokemon.trainer'
    _description = "Entrenador de pokemones"

    trainer_name = fields.Char(string="Nombre del entrenador", required = True)
    team = fields.One2many(comodel_name="pokemon.pokemon", inverse_name="trainer", required=True)