from odoo import fields, models


class SaleOrderOption(models.Model):
    _inherit = "sale.order.option"

    currency_id = fields.Many2one(related='order_id.currency_id')
