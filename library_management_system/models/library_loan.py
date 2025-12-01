from odoo import models,fields, api
from datetime import timedelta
from odoo.exceptions import UserError


class LibLoan(models.Model):
    _name = 'library.loan'

    partner_id = fields.Many2one(
        'res.partner',
        string='Độc giả',
        required=True,
    )
    book_id = fields.Many2one(
        'library.book',
        string ='Sách mượn',
        required=True,
    )
    date_start = fields.Date (default=fields.Date.context_today, string='Ngày bắt đầu')
    date_due = fields.Date(string= 'Hạn trả')
    days_until_due = fields.Integer(
        string='Ngày đến hạn',
        compute = '_compute_days_until_due_', 
        inverse='_inverse_days_until_due',
        store = False,)
    state = fields.Selection(
            [
                ('draft', 'Draft'),
                ('ongoing', 'Ongoing'),
                ('done', 'Done'),
                ('overdue', 'Overdue'),
            ],
            string="Trạng thái",
            default='draft',
            )

    @api.depends('date_due')
    def _compute_days_until_due_(self):
        today= fields.Date.today()
        for rec in self:
            if rec.date_due:
                rec.days_until_due = (rec.date_due - today).days
            else:
                rec.days_until_due = 0

    def action_confirm_state(self):
        for rec in self:
            if rec.state =='draft':
                rec.state = 'ongoing'
            elif rec.state == 'ongoing':
                rec.state = 'done'

    def _inverse_days_until_due(self):
        today = fields.Date.today()
        for rec in self:
            rec.date_due = today + timedelta(days=rec.days_until_due)
    
    def action_check_overdue(self):

        if any(rec.state != 'ongoing' for rec in self):
            raise UserError("This action is only valid for Ongoing items that have expired.")
        
        today = fields.Date.today()

        overdue_loans = self.env['library.loan'].search([
            ('state','=','ongoing'),
            ('date_due','<',today),
        ])
        
        overdue_loans.write({'state': 'overdue'})

class LibLoanWizard(models.TransientModel):
    _name ='library.loan.wizard'
    _inherit = 'library.loan'

    def action_confirm(self):
        self.env['library.loan'].create({
            'partner_id': self.partner_id.id,
            'book_ids': [(6, 0,self.book_ids.ids)],
        })

