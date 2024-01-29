# -*- coding: utf-8 -*-
# from odoo import http


# class Mecanico(http.Controller):
#     @http.route('/mecanico/mecanico', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/mecanico/mecanico/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('mecanico.listing', {
#             'root': '/mecanico/mecanico',
#             'objects': http.request.env['mecanico.mecanico'].search([]),
#         })

#     @http.route('/mecanico/mecanico/objects/<model("mecanico.mecanico"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('mecanico.object', {
#             'object': obj
#         })

