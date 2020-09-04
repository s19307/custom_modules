# -*- coding: utf-8 -*-
# from odoo import http


# class S19307Hr(http.Controller):
#     @http.route('/s19307_hr/s19307_hr/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/s19307_hr/s19307_hr/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('s19307_hr.listing', {
#             'root': '/s19307_hr/s19307_hr',
#             'objects': http.request.env['s19307_hr.s19307_hr'].search([]),
#         })

#     @http.route('/s19307_hr/s19307_hr/objects/<model("s19307_hr.s19307_hr"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('s19307_hr.object', {
#             'object': obj
#         })
