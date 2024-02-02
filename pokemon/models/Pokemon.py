# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Pokemon(models.Model):
    _inherit = "pokemon.species"

    _name = 'pokemon.pokemon'
    _description = "Un pokemon concreto"

    nickname = fields.Char(string="Mote")
    ability = fields.Many2one(comodel_name="pokemon.abilities", required=True)
    trainer = fields.Many2one(comodel_name="pokemon.trainer")

    possible_State = [
        ("1", "Wild"),
        ("2", "Captured")
    ]

    pokedex_number = fields.Integer(string="Numero de Pokedex Nacional", required=True)

    type_1 = fields.Many2one(comodel_name="pokemon.types", string="Primer tipo del pokemon" , related="specie.type_1", readonly=True, store=False)
    type_2 = fields.Many2one(comodel_name="pokemon.types", string="Segundo tipo del pokemon", related="specie.type_2", readonly=True, store=False)
    # api depends de si tiene trainer entonces no es salvaje, sino capturado

    state = fields.Selection(possible_State, string="Estado", required=True, default="1")
    # state = fields.Char(string ="seleccion")

    specie = fields.Many2one(comodel_name="pokemon.species", string="Especie", required=True)
