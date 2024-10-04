from odoo import fields, models

class WorkshopExpert(models.Model):
    _name = 'workshop.expert'
    _description = 'Workshop Expert'

    name = fields.Char(string="Expert Name", required=True)
    description = fields.Text(string="Description")
    expertise = fields.Char(string="Expertise")
    image = fields.Image(string="Expert Image")