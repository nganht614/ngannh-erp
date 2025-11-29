from odoo import models,fields,api
from odoo.exceptions import ValidationError

class ListActors(models.Model):
    _name = 'list.actor'
    _description ='Actors'

    name = fields.Char(string ='Actors')
    image = fields.Image(string='Avatar')
    gender = fields.Selection(
    [
        ('male', 'Nam'),
        ('female', 'Nữ'),
        ('other', 'Khác'),
    ],
    string='Giới tính',
    default = 'other',
    )
    date_of_birth = fields.Date(string ='Ngày sinh')
    age = fields.Integer(string='Tuổi', compute='_compute_age', store=True)
    biography = fields.Text(string='Tiểu sử')
    active = fields.Boolean(string='Có hiệu lực', compute ='_compute_active', store =True)
    country= fields.Char( string ='Quốc tịch')
    phone=fields.Integer(string='Liên hệ')
    email = fields.Char(string='Email')
    movie_ids = fields.One2many(
        'list.actor.movie', 'movie_id', 
        string ='Danh sách phim từng tham gia'
    )
    award_ids = fields.One2many(
        'list.actor.award',
        'name',
        string ='Tên giải thưởng'
    )
    _sql_constraints = [
         ('unique_email','unique(email)', 'Email đã tồn tại')
    ]

    @api.depends('date_of_birth')
    def _compute_age(self):
        today = fields.Date.today()
        for rec in self:
            if rec.date_of_birth:
                rec.age = today.year - rec.date_of_birth.year
            else:
                rec.age = 0
    @api.depends('age')
    def _compute_active(self):
        for rec in self:
                rec.active = rec.age <= 100
    @api.constrains('date_of_birth')
    def _check_dob(self):
        for rec in self:
            if rec.date_of_birth and rec.date_of_birth > fields.Date.today():
                raise ValidationError("Ngày sinh không được lớn hơn hôm nay!")
    @api.contrains('name','date_of_birth')
    def _check_duplicate_info(self):
        for rec in self:
            if rec.name and rec.date_of_birth:
                exists = self.search_count([
                    ('name', '=', rec.name),
                    ('date_of_birth', '=', rec.date_of_birth),
                    ('id', '!=', rec.id)
                ])
                if exists:
                    raise ValidationError("Diễn viên với cùng tên và ngày sinh đã tồn tại!")
    @api.onchange('date_of_birth')
    def _onchange_age(self):
        for rec in self:
            today = fields.Date.today()
            if rec.date_of_birth:
                rec.age = today.year - rec.date_of_birth.year
            else:
                rec.age = 0