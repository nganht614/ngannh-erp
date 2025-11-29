from odoo import models,fields

class Exam(models.Model):
    _name='exam'
    _description='Exam'

    name = fields.Char(string='Name')
    subject= fields.Char(string='Môn học')
    score= fields.Integer(string= 'Score')