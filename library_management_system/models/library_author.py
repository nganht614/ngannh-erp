from odoo import models,fields

class LibAuthor(models.Model):
    _name ='library.author'

    name = fields.Char(string ='Tên tác giả', required=True)
    book_ids = fields.One2many('library.book', 'author_id')

    def action_view_stats(self):

        books = self.book_ids.mapped('name') 
        long_books = len(self.book_ids.filtered(lambda b: b.pages > 500))
        return {
        'books': books,
        'long_books': long_books,
        }