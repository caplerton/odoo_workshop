from odoo import models, fields

class WorkshopFeeback(models.Model):
    _name = 'workshop.session.feedback'
    
    session_id = fields.Many2one('workshop.session', string="Session", required=True)
    # rating = fields.Selection([(str(i), str(i)) for i in range(1, 6)], string='Bewertung', required=True)
    feedback_text = fields.Text('Feedback')
    expert_rating = fields.Integer(string="Expert rating", required=True, default=-1)
    workshop_rating = fields.Integer(string="Workshop rating", required=True, default=-1)
    