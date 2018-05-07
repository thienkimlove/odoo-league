# -*- coding: utf-8 -*-

from odoo import models, fields, api

class TimeModel(models.AbstractModel):

    _order = 'sequence,name'

    name = fields.Char('Name')
    sequence = fields.Integer('Sequence', default=0)
    status = fields.Boolean('Active?', default=True)

    updated_at = fields.Datetime(
        'Updated Date and Time',
        default=lambda self: fields.Datetime.now())
    created_at = fields.Datetime(
        'Create Date and Time',
        default=lambda self: fields.Datetime.now())


class Category(TimeModel):
