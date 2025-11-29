from odoo import models,fields

class ActorMovie(models.Model):
    __name = 'list.actor.movie'

    actor_id = fields.Many2one(
        'list.actor',
        string ='Diễn viên',
    )
    movie_id = fields.Many2one(
        'list.movie',
        string = 'Phim',
    )
    role_name = fields.Char(string ='Vai diễn')
    is_main_role = fields.Boolean(string='Đây là vai chính')
    salary = fields.Float(string = 'Thù lao')
    