from odoo import models, fields, api

class TimeSlot(models.Model):
    """Model to store Timeslots."""
    _name = "workshop.session.timeslot"
    _description = "Session Timeslot"
    
    start_time = fields.Datetime(string="Start Time", required=True)
    end_time = fields.Datetime(string="End Time", required=True)
    session_id = fields.Many2one('workshop.session', string="Session", required=True)
    name = fields.Char("Workshop name", related="session_id.workshop_name",  required=True)
    # name = fields.Char("Workshop name", related="session_id.name" )
    # session = fields.Char("Session", related="session_id")
    # display_name = fields.Char(string='Display Name', compute='_compute_display_name')

    # @api.depends('name', 'workshop_id')
    # def _compute_display_name(self):
    #     for record in self:
    #         record.display_name = f"Session: {self.session_id.name}"
