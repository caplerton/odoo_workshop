from odoo import fields, models

class Workshop(models.Model):
    _name = "workshop.workshop"
    _description = "Workshop element"
    
    
    name = fields.Char(string="Name", required=True)
    description = fields.Text(string="Description")
    
    image = fields.Image(string="Workshop Image")
    # file = fields.Binary(string="Attached File")
    file_name = fields.Char(string="File Name")
    
    file = fields.Binary(string='Attachenment' )