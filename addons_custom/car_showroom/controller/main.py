
# **Giải thích**:
# - **Snippet `car_showroom_featured_cars_snippet`**: Hiển thị 3 xe có `stock > 0`, có thể kéo thả vào trang chủ.
# - **Đăng ký snippet**: Thêm snippet vào nhóm "Features" trong Website Builder.
# - **Template `car_showroom_list`**: Trang danh sách xe với bộ lọc theo thương hiệu và tồn kho.
# - **Template `car_showroom_detail`**: Trang chi tiết xe dựa trên `id`.
# - **Menu `car_showroom_menu`**: Tạo mục menu "Cars" dẫn đến `/cars`.

##### **5. Tạo file `controllers/main.py`**

# Tạo file `D:\Odoo\odoo-18.0\addons_custom\car_showroom\controllers\main.py`:

# ```python
from odoo import http
from odoo.http import request
import logging
_logger = logging.getLogger(__name__)

class CarShowroomController(http.Controller):
    print("✅ Controller loaded")
    @http.route('/cars', type='http', auth='public', website=True)
    
    def car_list(self, **kwargs):
        # Lấy tất cả xe cho danh sách
        cars = request.env['car.showroom'].sudo().search([])
        # Lấy 3 xe có stock lớn nhất (stock > 0)
        featured_cars = request.env['car.showroom'].sudo().search([('stock', '>', 0)], order='stock desc', limit=3)
        return request.render('car_showroom.car_showroom_list', {
            'cars': cars,
            'featured_cars': featured_cars
        })

    @http.route('/car/<int:car_id>', type='http', auth='public', website=True)
    def car_detail(self, car_id, **kwargs):
        car = request.env['car.showroom'].sudo().browse(car_id)
        if not car.exists():
            return request.render('website.page_404', {})
        return request.render('car_showroom.car_showroom_detail', {
            'car': car,
        })

    
#     Giải thích:

# Route /cars: Lấy danh sách xe từ model car.showroom, áp dụng bộ lọc (thương hiệu, tồn kho), render template car_showroom_list.
# Route /car/<int:car_id>: Hiển thị chi tiết xe dựa trên id, trả về trang 404 nếu xe không tồn tại.