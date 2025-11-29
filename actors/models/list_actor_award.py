from odoo import models,fields

class Awards(models.Model):
    _name ='list.actor.award'

    actor_id = fields.Many2one(
        'list.actor',
        string ='Diễn viên'
    )
    name = fields.Char(string='Tên giải thưởng')
    year = fields.Integer(string='Năm')
    description = fields.Char(string='Mô tả')
