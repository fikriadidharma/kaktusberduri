# -*- coding: utf-8 -*-

from odoo import models, fields, api

STATE = [
    ('draft', 'Draft'),
    ('done', 'Done'),
]

class Task(models.Model):
    _name = 'to_do_list.task'

    title = fields.Char(string='Title', required=True)
    # value = fields.Integer()
    # value2 = fields.Float(compute="_value_pc", store=True)
    description = fields.Text(string='Description')
    check = fields.Selection(STATE, default=STATE[0][0], required=True)
    date_creation = fields.Date('Created Date', required=True, default=fields.Date.today())
