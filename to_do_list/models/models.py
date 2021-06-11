# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Task(models.Model):
    _name = 'to_do_list.task'

    title = fields.Char(string='Title', required=True)
    # value = fields.Integer()
    # value2 = fields.Float(compute="_value_pc", store=True)
    description = fields.Text(string='Description')
    check = fields.Boolean(string='Boolean')
