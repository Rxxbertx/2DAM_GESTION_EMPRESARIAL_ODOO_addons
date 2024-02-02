# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Specie(models.Model):


    _name = 'pokemon.specie'
    _description = "Especies de pokemones"

    name = fields.Char(string="Nombre", required=True)

    pokedex_number = fields.Integer(string="Numero de Pokedex Nacional", required=True, default=lambda self: self._get_next_pokedex_number())

    img = fields.Image(string="Imagen")

    ability = fields.Many2many(comodel_name="pokemon.ability", string="Habilidades")

    hidden_ability = fields.Many2one(comodel_name="pokemon.ability", string="Habilidad Oculta", compute="_compute_hidden_ability", store=True)

    type_1 = fields.Many2one(comodel_name="pokemon.type", string="Primer tipo del pokemon")

    type_2 = fields.Many2one(comodel_name="pokemon.type", string="Segundo tipo del pokemon")

    atk = fields.Integer(string="Ataque")

    hp = fields.Integer(string="Puntos de Vida")

    defense = fields.Integer(string="Defensa")

    last_pokedex_number = fields.Integer(string="Último número de Pokedex", default=0)

    @api.depends('ability')
    def _compute_hidden_ability(self):
        for record in self:
            if record.ability:
                record.hidden_ability = record.ability[-1].id
            else:
                record.hidden_ability = False

    @api.model
    def _get_next_pokedex_number(self):
        last_number = self.search([], order='pokedex_number desc', limit=1).pokedex_number
        return last_number + 1 if last_number else 1