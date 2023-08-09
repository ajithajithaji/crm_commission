# -*- coding: utf-8 -*-
from odoo import fields, models


class RevenueWise(models.Model):
    """Create a model"""
    _name = 'revenue.wise'
    _description = 'Revenue Wise'

    sequence = fields.Integer(string='Sequence', required=True)
    from_amount = fields.Float(string='From Amount', required=True)
    to_amount = fields.Float(string='To Amount', required=True)
    rate = fields.Float(string='Rate', required=True)
    commission_id = fields.Many2one('crm.commission', string='Commission')
