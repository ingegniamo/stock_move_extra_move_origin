

from odoo import _, api, Command, fields, models


class StockMove(models.Model):
    _inherit = "stock.move"
    def _prepare_extra_move_vals(self, qty):
        vals = super()._prepare_extra_move_vals(qty)
        vals['origin'] = self.origin
        return vals