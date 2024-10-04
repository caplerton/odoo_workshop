from odoo import fields, models

class WorkshopExpert(models.Model):
    _name = 'workshop.expert'
    _description = 'Workshop Expert'

    name = fields.Char(string="Expert Name", required=True)
    description = fields.Text(string="Description")
    expertise = fields.Char(string="Expertise")
    image = fields.Image(string="Expert Image")
    workshop_ids = fields.Many2many('workshop.workshop', string="Workshops" , readonly=True)
    seesion_id = fields.One2many('workshop.session','expert_id',string="Session", readonly=True)
    