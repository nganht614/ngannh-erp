from odoo import models,fields

class LibCategr(models.Model):
    _name = 'library.category'

    name = fields.Char(string ='Loại', required=True)