from odoo import models,fields

class LibAuthor(models.Model):
    _name ='library.author'

    name = fields.Char('Tên tác giả')
    book_ids = fields.One2many('library.book', 'name')