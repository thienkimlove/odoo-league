# -*- coding: utf-8 -*-
from odoo import http

# class Generation(http.Controller):
#     @http.route('/generation/generation/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/generation/generation/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('generation.listing', {
#             'root': '/generation/generation',
#             'objects': http.request.env['generation.generation'].search([]),
#         })

#     @http.route('/generation/generation/objects/<model("generation.generation"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('generation.object', {
#             'object': obj
#         })