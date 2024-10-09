from io import BytesIO
import qrcode
from odoo import api, fields, models
from PIL import Image 
import base64

class WorkshopSession(models.Model):
    _name = 'workshop.session'
    _description = 'Workshop Session'

    name = fields.Char(string="Session Name", required=True)
    description = fields.Text(string="Description")
    # start_time = fields.Datetime(string="Start Time", required=True)
    # end_time = fields.Datetime(string="End Time", required=True)
    expert_id = fields.Many2one('workshop.expert', string="Expert", required=True)
    workshop_ids = fields.Many2one('workshop.workshop', string="Workshops", required=True)
    workshop_name = fields.Char("Workshop name", related="workshop_ids.name" )

    time_ids = fields.One2many("workshop.session.timeslot", "session_id", string="Timeslots")
    feedback_id = fields.One2many('workshop.session.feedback', "session_id")
    
    session_feedback_url = fields.Char(string='Feedback URL', compute="_compute_url")
    session_feedback_qr = fields.Image(string="Feedback QR", compute="_compute_qr")
    
    
    def _get_url(self) -> str:
        base_url = self.env['ir.config_parameter'].sudo().get_param('web.base.url')
        return f"{base_url}/feedback/{self.id}"
    
    
    def _compute_qr(self) -> None:
        img = qrcode.make(self._get_url())
        # img = img.resize((300,300), Image.ANTIALIAS)
        buffer = BytesIO()
        img.save(buffer, format="PNG")
        img_bytes = buffer.getvalue()
        img_base64 = base64.b64encode(img_bytes).decode('utf-8')
        self.session_feedback_qr=  img_base64
        
    
        
    # @api.depends('id')
    def _compute_url(self) ->  None:
        # base_url = self.env['ir.config_parameter'].sudo().get_param('web.base.url')
        self.session_feedback_url= self._get_url()
        
    
    

        
            
