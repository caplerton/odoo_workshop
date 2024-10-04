from odoo import fields, models

class WorkshopSession(models.Model):
    _name = 'workshop.session'
    _description = 'Workshop Session'

    name = fields.Char(string="Expert Name", required=True)
    description = fields.Text(string="Description")
    start_time = fields.Datetime(string="Start Time", required=True)
    end_time = fields.Datetime(string="End Time", required=True)
    expert_id = fields.Many2one('workshop.expert', string="Expert", required=True)
    workshop_ids = fields.Many2one('workshop.workshop', string="Workshops", required=True)
