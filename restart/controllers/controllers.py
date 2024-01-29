# -*- coding: utf-8 -*-
# from odoo import http


# class Restart(http.Controller):
#     @http.route('/restart/restart', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/restart/restart/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('restart.listing', {
#             'root': '/restart/restart',
#             'objects': http.request.env['restart.restart'].search([]),
#         })

#     @http.route('/restart/restart/objects/<model("restart.restart"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('restart.object', {
#             'object': obj
#         })
