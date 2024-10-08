from odoo import api, fields, models

class WorkshopSession(models.Model):
    _name = 'workshop.session'
    _description = 'Workshop Session'

    name = fields.Char(string="Expert Name", required=True)
    description = fields.Text(string="Description")
    start_time = fields.Datetime(string="Start Time", required=True)
    end_time = fields.Datetime(string="End Time", required=True)
    expert_id = fields.Many2one('workshop.expert', string="Expert", required=True)
    workshop_ids = fields.Many2one('workshop.workshop', string="Workshops", required=True)

    sequence_number = fields.Char('Sequenznummer', readonly=True, copy=False)

    feedback_id = fields.One2many('workshop.session.feedback', "session_id")
    @api.model
    def create(self, vals):
        
        if not vals.get('sequence_number'):
            vals['sequence_number'] = "session_0"
        return super(WorkshopSession, self).create(vals)