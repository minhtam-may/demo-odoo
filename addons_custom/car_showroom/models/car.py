from odoo import models, fields
from odoo.exceptions import UserError
class CarShowroom(models.Model):
    _name = 'car.showroom'
    _description = 'Car Showroom'

    name = fields.Char(string='Tên xe', required=True)
    brand = fields.Char(string='Hãng xe')
    price = fields.Float(string='Giá (VND)')
    stock = fields.Integer(string='Số lượng tồn kho')
    image = fields.Image(string='Hình ảnh')

    def increase_stock(self):
        self.stock += 1

    def decrease_stock(self):
        if self.stock > 0:
            self.stock -= 1
    
