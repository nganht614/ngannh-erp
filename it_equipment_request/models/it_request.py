from odoo import models,fields,api

class ItRequest(models.Model):
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
        # inverse ='_inverse_total_amount_',
        store =True,
        string ='Tổng',)
    
    _sql_constraints = [
        ('check_total_amount','CHECK(total_amount < 100000000)', 'Tổng tiền không được vượt quá 100 triệu')
    ]

    @api.onchange('employee_id')
    def _onchange_department_(self):
        self.department_id = self.employee_id.department_id

    @api.depends('line_ids.price')
    def _compute_total_amount_(self):
        for rec in self:
            rec.total_amount = sum(rec.line_ids.mapped('price'))
