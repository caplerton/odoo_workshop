from odoo import fields, models

class Workshop(models.Model):
    _name = "workshop.workshop"
    
    name = fields.Char(string="Name", required=True)
    description = fields.Text(string="Description")