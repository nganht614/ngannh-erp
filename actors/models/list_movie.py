from odoo import models,fields

class Movies(models.Model):
    _name ='list.movie'

    name = fields.Char(string='Tên phim')
    release_date = fields.Date(string='Ngày phát hành')
    description = fields.Char(string='Mô tả phim')
    actor_ids = fields.One2many(
        'list.actor.movie',
        'actor_id',
        string ='Diễn viên'
    )
    