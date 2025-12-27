from odoo import models, fields

class ItEquipment(models.Model):
    _name = 'it.equipment'

    name = fields.Char(string='Tên thiết bị')
    code = fields.Char(string='Mã thiết bị')
    price = fields.Float(string='Giá')
    quantity = fields.Integer(string='Số lượng')
    active = fields.Boolean(string='Đang hoạt động', default=True)
    