from odoo import models,fields,api
from odoo.exceptions import ValidationError

class LibArchMixin(models.AbstractModel):
    _name = 'library.archivable.mixi'
    _abstract = True

    archive_date = fields.Date(string= 'Ngày lưu trữ')

    def action_archive(self):
        self.write({'archive_date': fields.Date.today()})

class LibraryManagement(models.Model):
    _name ='library.book'
    _inherit = ['library.archivable.mixi']

    name = fields.Char(string ='Tên sách', required=True)
    isbn = fields.Char(string ='Mã sách')
    active = fields.Boolean(string ='Trạng thái kích hoạt', default=True)
    published_date = fields.Date(string ='Ngày xuất bản')
    pages = fields.Integer(string='Số trang')
    description = fields.Html (string='Mô tả nội dung')
    author_id = fields.Many2one(
        'library.author',
        string ='Tên tác giả',
    )
    category_ids = fields.Many2many(
        'library.category',
        string = 'Loại sách',
    )
    _sql_constraints = [
         ('unique_isbn','unique(isbn)', 'Mã sách đã tồn tại')
    ]

    @api.constrains('published_date')
    def _check_pub_date(self):
        for rec in self:
            if rec.published_date and rec.published_date > fields.Date.today():
                raise ValidationError ('Ngày xuất bản không được lớn hơn ngày hiện tại')
    
    @api.constrains('isbn')
    def _check_unique_isbn(self):
        for rec in self:
            if not rec.isbn:
                continue
            domain = [
                ('isbn', '=', rec.isbn),
                ('id', '!=', rec.id)
            ]
            if self.search_count(domain) > 0:
                raise ValidationError("Mã đã tồn tại!")