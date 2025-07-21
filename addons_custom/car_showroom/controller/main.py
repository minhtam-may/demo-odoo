from odoo import http

class CarShowroom(http.Controller):
    @http.route('/cars', auth='public', website=True)
    def car_list(self, **kw):
        # Lấy danh sách sản phẩm
        all_products = http.request.env['product.template'].sudo().search([
            ('list_price', '>', 0),  # Điều kiện ví dụ
        ])
        featured_products = all_products.filtered(lambda p: p.qty_available > 0)[:4]
        products = all_products

        # Truyền context với currency
        return http.request.render('car_showroom.car_showroom_list', {
            'featured_products': featured_products,
            'products': products,
            'currency': http.request.env.company.currency_id,
        })

    @http.route('/car/<int:product_id>', auth='public', website=True)
    def car_detail(self, product_id, **kw):
        # Lấy chi tiết sản phẩm
        car = http.request.env['product.template'].sudo().browse(product_id)
        return http.request.render('car_showroom.car_showroom_detail', {
            'car': car,
            'currency': http.request.env.company.currency_id,
        })