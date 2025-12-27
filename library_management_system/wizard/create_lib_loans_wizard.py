from odoo import models, fields, api
from odoo.exceptions import UserError

class LibLoanWizard(models.TransientModel):
    _name ='library.loan.wizard'

    partner_id = fields.Many2one(
        'res.partner',
        string='Độc giả',
        required=True,
    )
    book_ids = fields.Many2many('library.book', string='Danh sách')
    date_due = fields.Date(string='Hạn trả',required=True)

    def action_confirm(self):

        self.ensure_one()

        for book in self.book_ids:
            self.env['library.loan'].create({
                'partner_id': self.partner_id.id,
                'book_id': book.id,
                'date_due': self.date_due,
            })
    

