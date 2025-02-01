from odoo import models,fields, api

class new_sale_order(models.Model):
    _inherit = 'sale.order'

    confirmed_user_id = fields.Many2one('res.users', string='Confirmed User')