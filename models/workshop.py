from odoo import fields, models

class Workshop(models.Model):
    _name = "workshop.workshop"
    _description = "Workshop element"
    
    
    name = fields.Char(string="Name", required=True)
    description = fields.Text(string="Description")
    
    image = fields.Image(string="Workshop Image")
    # file = fields.Binary(string="Attached File")
    # file_name = fields.Char(string="File Name")
    
    # file = fields.Binary(string='Attachenment' )
    attachment_ids = fields.Many2many(
        comodel_name="ir.attachment",
        string="Attachments",
        relation="workshop_attachment_rel",
        column1="workshop_id",
        column2="attachment_id",
        domain="[('res_model', '=', 'workshop.workshop')]"
    )