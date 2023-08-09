# -*- coding: utf-8 -*-
from odoo import fields, models


class CrmCommission(models.Model):
    """Create a model crm commission"""
    _name = 'crm.commission'
    _description = 'Crm Commission'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Name', required=True)
    active = fields.Boolean(string='Active', default=True)
    from_date = fields.Date(string='From Date', required=True)
    to_date = fields.Date(string='To Date', required=True)
    commission_type = fields.Selection(
        [('product_wise', 'Product wise'),
         ('revenue_wise', 'Revenue Wise')], string='Type', required=True)
    product_wise_ids = fields.One2many('product.wise',
                                       'crm_commission_id',
                                       string='Product Wise')
    revenue_type = fields.Selection(
        [('straight', 'Straight'), ('graduated', 'Graduated')])
    revenue_wise_ids = fields.One2many('revenue.wise',
                                       'commission_id',
                                       string='Revenue Wise')
