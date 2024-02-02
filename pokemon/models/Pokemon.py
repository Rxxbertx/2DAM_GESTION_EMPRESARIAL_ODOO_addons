# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Pokemon(models.Model):
    _inherit = "pokemon.specie"

    _name = 'pokemon.pokemon'
    _description = "Un pokemon concreto"

    nickname = fields.Char(string="Apodo")
    specie = fields.Many2one(comodel_name="pokemon.specie", required=True, string="Especie")

    pokedex_number = fields.Integer(related='specie.pokedex_number', string="Numero de Pokedex Nacional")
    name = fields.Char(related='specie.name', string="Nombre Especie")
    pokemon_ability = fields.Many2one(comodel_name="pokemon.ability", required=True, string="Habilidad Pokemon")
    trainer = fields.Many2one(comodel_name="pokemon.trainer", required=True, string="Entrenador")
    img = fields.Image(string="Imagen")
    ability = fields.Many2many(related='specie.ability', string="Habilidades")
    hidden_ability = fields.Many2one(related='specie.hidden_ability', string="Habilidad Oculta")
    type_1 = fields.Many2one(related='specie.type_1', string="Primer tipo del pokemon")
    type_2 = fields.Many2one(related='specie.type_2', string="Segundo tipo del pokemon")
    atk = fields.Integer(related='specie.atk', string="Ataque")
    hp = fields.Integer(related='specie.hp', string="Puntos de Vida")
    defense = fields.Integer(related='specie.defense', string="Defensa")
    last_pokedex_number = (fields.Integer(related='specie.last_pokedex_number', string="Último número de Pokedex"))

    @api.constrains('atk', 'defense', 'hp')
    def _check_stats(self):
        for record in self:
            if record.atk < 0:
                record.atk = 0
            if record.defense < 0:
                record.defense = 0
            if record.hp < 0:
                record.hp = 0
            if record.defense > record.atk:
                record.defense = record.atk
            if record.hp > record.atk:
                record.hp = record.atk
