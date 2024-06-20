from odoo import models, fields

class Penumpang(models.Model):
    _name = "Penumpang Transportasi"
    _description = 'Model Technical Name'

name = fields.Char('Name',size=32, help='Nama Penumpang')
born_date = fields.Date('Born Date')
weight = fields.Float('Weight')
height = fields.Float('Height')
state = fields.Selection([
    ('general', 'General'),('member', 'Member')
], 'State', default="general")
id_number = fields.Char('Id Number', size=32, required=1 )