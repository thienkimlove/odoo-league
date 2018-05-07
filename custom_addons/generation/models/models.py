# -*- coding: utf-8 -*-

from odoo import models, fields, api

class TimeModel(models.AbstractModel):

    _order = 'sequence,name'

    name = fields.Char('Name')
    sequence = fields.Integer('Sequence', default=0)
    active = fields.Boolean('Active?', default=True)

class Category(TimeModel):
