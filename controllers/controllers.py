# -*- coding: utf-8 -*-
# from odoo import http


# class Clipmetrajes(http.Controller):
#     @http.route('/clipmetrajes/clipmetrajes/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/clipmetrajes/clipmetrajes/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('clipmetrajes.listing', {
#             'root': '/clipmetrajes/clipmetrajes',
#             'objects': http.request.env['clipmetrajes.clipmetrajes'].search([]),
#         })

#     @http.route('/clipmetrajes/clipmetrajes/objects/<model("clipmetrajes.clipmetrajes"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('clipmetrajes.object', {
#             'object': obj
#         })
