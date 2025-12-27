from odoo import models,fields,api
from odoo.exceptions import ValidationError

class ItRequestLine(models.Model):
    _name ='it.request.line'

    request_id = fields.Many2one(
        'it.request',
        string= 'Yêu cầu',
    )
    equipment_id = fields.Many2one(
        'it.equipment',
        string='Thiết bị',
    )
    price = fields.Float(string='Giá', readonly=True)
    quantity = fields.Integer(string = 'Số lượng')
    subtotal = fields.Float(string ='Tổng')


    @api.onchange('equipment_id')
    def _onchange_price(self):
        self.price = self.equipment_id.price

    @api.constrains('equipment_id', 'request_id')
    def _check_unique_equip(self):
        for rec in self:
            if not rec.equipment_id or not rec.request_id:
                continue
            domain = [
                ('request_id', '=', rec.request_id.id),
                ('equipment_id', '=', rec.equipment_id.id),
            ] 
            if self.search_count(domain) > 1:
                raise ValidationError("Thiết bị này đã được chọn")

