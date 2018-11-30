# -*- coding: utf-8 -*-
from odoo import http

# class XmartsAutoSeries(http.Controller):
#     @http.route('/xmarts_auto_series/xmarts_auto_series/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/xmarts_auto_series/xmarts_auto_series/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('xmarts_auto_series.listing', {
#             'root': '/xmarts_auto_series/xmarts_auto_series',
#             'objects': http.request.env['xmarts_auto_series.xmarts_auto_series'].search([]),
#         })

#     @http.route('/xmarts_auto_series/xmarts_auto_series/objects/<model("xmarts_auto_series.xmarts_auto_series"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('xmarts_auto_series.object', {
#             'object': obj
#         })