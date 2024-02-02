# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Specie(models.Model):


    _name = 'pokemon.specie'
    _description = "Especies de pokemones"

    name = fields.Char(string="Nombre", required=True)
    img = fields.Image(string="Imagen")
    pokedex_number = fields.Integer(string="Numero de Pokedex Nacional", required=True)
    ability = fields.Many2many(comodel_name="pokemon.ability", string="Habilidades")
    hidden_ability = fields.Many2one(comodel_name="pokemon.abilities", string="Habilidad Oculta", compute="_compute_hidden_ability", store=True)
    type_1 = fields.Many2one(comodel_name="pokemon.types", string="Primer tipo del pokemon")
    type_2 = fields.Many2one(comodel_name="pokemon.types", string="Segundo tipo del pokemon")
    atk = fields.Integer(string="Ataque")
    hp = fields.Integer(string="Puntos de Vida")
    defense = fields.Integer(string="Defensa")



    @api.depends('ability')
    def _compute_hidden_ability(self):
        for record in self:
            print(record.abilities[-1], record.abilities[-1].id)
            if record.abilities:
                record.hidden_ability = record.abilities[-1].id
            else:
                record.hidden_ability = False

