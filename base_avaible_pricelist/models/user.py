# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models


class Users(models.Model):
    _inherit = "res.users"

    pricelist_ids = fields.Many2many('product.pricelist', string='Pricelist')

