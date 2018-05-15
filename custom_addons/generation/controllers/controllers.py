# -*- coding: utf-8 -*-
from odoo import http
from odoo.addons.web.controllers.main import Home


class Generation(Home):
    #@http.route('/generation', auth='none')
    @http.route(['/', '/index', '/home'],  auth='public')
    def index(self, **kw):
        records = http.request.env['generation.post'].sudo().search([])
        return http.request.render('generation.index', {
                 'records': records,
             })

