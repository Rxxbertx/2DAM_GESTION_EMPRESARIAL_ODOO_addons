# -*- coding: utf-8 -*-
# from odoo import http


# class BibliotecaRoberto(http.Controller):
#     @http.route('/biblioteca_roberto/biblioteca_roberto', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/biblioteca_roberto/biblioteca_roberto/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('biblioteca_roberto.listing', {
#             'root': '/biblioteca_roberto/biblioteca_roberto',
#             'objects': http.request.env['biblioteca_roberto.biblioteca_roberto'].search([]),
#         })

#     @http.route('/biblioteca_roberto/biblioteca_roberto/objects/<model("biblioteca_roberto.biblioteca_roberto"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('biblioteca_roberto.object', {
#             'object': obj
#         })

