from odoo import models,fields

class LibLoan(models.Model):
    _name = 'library.loan'

    partner_id = fields.Many2one(
        'res.partner',
        string='Độc giả'
    )
    book_id = fields.Many2one(
        'library.book',
        string ='Sách mượn',
    )
    date_start = fields.Date (default )