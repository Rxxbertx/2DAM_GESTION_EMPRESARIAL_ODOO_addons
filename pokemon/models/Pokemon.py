# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError


class Pokemon(models.Model):
    _name = 'pokemon.pokemon'
    _description = "Un pokemon concreto"

    nickname = fields.Char(string="Apodo", required=True)
    specie = fields.Many2one(comodel_name="pokemon.specie", required=True, string="Especie")

    name = fields.Char(related='specie.name', string="Nombre Especie", required=True)

    trainer = fields.Many2one(comodel_name="pokemon.trainer", required=True, string="Entrenador")
    img = fields.Image(string="Imagen")
    ability = fields.Many2many(related='specie.ability', string="Habilidades")
    hidden_ability = fields.Many2one(related='specie.hidden_ability', string="Habilidad Oculta")
    type_1 = fields.Many2one(related='specie.type_1', string="Primer tipo del pokemon")
    type_2 = fields.Many2one(related='specie.type_2', string="Segundo tipo del pokemon")
    atk = fields.Integer(string="Ataque", required=True)
    hp = fields.Integer(string="Puntos de Vida", required=True)
    defense = fields.Integer(string="Defensa", required=True)
    pokedex_number = fields.Integer(related='specie.pokedex_number', string="Número de Pokedex")
    pokemon_ability = fields.Many2one(
        comodel_name="pokemon.ability",
        string="Habilidad Pokemon"
    )

    @api.constrains('atk', 'defense', 'hp')
    def _check_stats(self):
        for record in self:
            if record.atk > record.specie.atk:
                record.atk = record.specie.atk
            elif record.atk < 0:
                record.atk = 0

            if record.defense > record.specie.defense:
                record.defense = record.specie.defense
            elif record.defense < 0:
                record.defense = 0

            if record.hp > record.specie.hp:
                record.hp = record.specie.hp
            elif record.hp < 0:
                record.hp = 0

    @api.constrains('trainer')
    def _check_trainer(self):
        for record in self:
            if len(record.trainer.team) > 6:
                raise ValidationError("Un entrenador no puede tener más de 6 pokémon.")

    @api.onchange('specie')
    def _onchange_specie(self):
        if self.specie:
            return {'domain': {'pokemon_ability': [('id', 'in', self.specie.ability.ids)]}}
        else:
            return {'domain': {'pokemon_ability': []}}