from odoo import models, fields
import logging
_logger = logging.getLogger(__name__)
class KenhBanHang(models.Model):
    _name = "kenh.ban.hang"
    _description = "Kênh bán hàng"

    name = fields.Char(string='Kênh bán hàng')
    description = fields.Text(string='Mô tả')
    ngay_thanh_lap = fields.Date(string='Ngày thành lập')
    doanh_thu = fields.Float(string='Doanh thu')
    so_thanh_vien = fields.Integer(string='Số lượng thành viên')
    active = fields.Boolean(default=True)
    trang_thai = fields.Selection(string='Trang thái', selection=[('active', 'Hoạt động'), ('deactive', 'Không hoạt động')])
    # lấy ra từ bảng res-user mặc định của odoo
    quan_ly = fields.Many2one('res.users', string='Người quản lý', index = True)
_logger.info("✅ kenh_ban_hang model loaded!")