# -*- coding: utf-8 -*-
from odoo import http

# class Nada(http.Controller):
#     @http.route('/nada/nada/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/nada/nada/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('nada.listing', {
#             'root': '/nada/nada',
#             'objects': http.request.env['nada.nada'].search([]),
#         })

#     @http.route('/nada/nada/objects/<model("nada.nada"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('nada.object', {
#             'object': obj
#         })