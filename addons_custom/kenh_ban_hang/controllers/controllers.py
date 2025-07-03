# -*- coding: utf-8 -*-
# from odoo import http


# class KenhBanHang(http.Controller):
#     @http.route('/kenh_ban_hang/kenh_ban_hang', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/kenh_ban_hang/kenh_ban_hang/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('kenh_ban_hang.listing', {
#             'root': '/kenh_ban_hang/kenh_ban_hang',
#             'objects': http.request.env['kenh_ban_hang.kenh_ban_hang'].search([]),
#         })

#     @http.route('/kenh_ban_hang/kenh_ban_hang/objects/<model("kenh_ban_hang.kenh_ban_hang"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('kenh_ban_hang.object', {
#             'object': obj
#         })

