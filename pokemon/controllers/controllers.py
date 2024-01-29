# -*- coding: utf-8 -*-
# from odoo import http


# class Pokemon(http.Controller):
#     @http.route('/pokemon/pokemon', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/pokemon/pokemon/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('pokemon.listing', {
#             'root': '/pokemon/pokemon',
#             'objects': http.request.env['pokemon.pokemon'].search([]),
#         })

#     @http.route('/pokemon/pokemon/objects/<model("pokemon.pokemon"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('pokemon.object', {
#             'object': obj
#         })
