# -*- coding: utf-8 -*-
from odoo import http

# class ConnectorNada(http.Controller):
#     @http.route('/connector_nada/connector_nada/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/connector_nada/connector_nada/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('connector_nada.listing', {
#             'root': '/connector_nada/connector_nada',
#             'objects': http.request.env['connector_nada.connector_nada'].search([]),
#         })

#     @http.route('/connector_nada/connector_nada/objects/<model("connector_nada.connector_nada"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('connector_nada.object', {
#             'object': obj
#         })