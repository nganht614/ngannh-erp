from odoo import models,fields

class itreq(models.Model):
    _name ='it.request'

    name = fields.Char(string ='Tên yêu cầu')
    employee_id = fields.Many2one(
        'hr.employee',
        string= 'Tên nhân viên',
        required =True,
    )
    department_id = fields.Many2one(
        'hr.department',
        string='Phòng ban',
    )
    request_date = fields.Date(string = 'Ngày yêu cầu')
    approve_date = fields.Date(string='Ngày phê duyệt')
    state = fields.Selection(
        [
            ("draft", "Draft"),
            ('waiting', 'Waiting'),
            ('approved', 'Approved'),
            ('rejected', 'Rejected'),
        ]
    )
    line_ids = fields.One2many(
        'it.request.line', 
        'request_id',
        string= 'Chi tiết'
    )
    total_amount = fields.Float(
        compute ='_compute_total_amount_', 
        inverse ='_inverse_total_amount',
        store =True,
        string ='Tổng',)
