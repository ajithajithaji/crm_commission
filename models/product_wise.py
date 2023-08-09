# -*- coding: utf-8 -*-
from odoo import fields, models


class ProductWise(models.Model):
    """Create a model productWise for commission rate and different products"""
    _name = 'product.wise'
    _description = 'Product Wise'

    product_id = fields.Many2one('product.template',
                                 string='Product', required=True)
    product_category_id = fields.Many2one('product.category',
                                          string='Product Category',
                                          required=True,
                                          related='product_id.categ_id')
    rate_percentage = fields.Float(string='Rate (%)')
    max_commission_amount = fields.Float(string='Maximum Commission Amount')
    crm_commission_id = fields.Many2one('crm.commission',
                                        string='Crm Commissions')
