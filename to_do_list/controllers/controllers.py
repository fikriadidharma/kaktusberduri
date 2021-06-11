# -*- coding: utf-8 -*-
from odoo import http

# class ToDoList(http.Controller):
#     @http.route('/to_do_list/to_do_list/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/to_do_list/to_do_list/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('to_do_list.listing', {
#             'root': '/to_do_list/to_do_list',
#             'objects': http.request.env['to_do_list.to_do_list'].search([]),
#         })

#     @http.route('/to_do_list/to_do_list/objects/<model("to_do_list.to_do_list"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('to_do_list.object', {
#             'object': obj
#         })