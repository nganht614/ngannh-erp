from odoo import models,fields

class LibReaders(models.Model):
    _inherit = 'res.partner'

    is_library_member = fields.Boolean(string = 'Là thành viên')
    library_card_code = fields.Char(string= 'Mã thẻ thư viện')
    