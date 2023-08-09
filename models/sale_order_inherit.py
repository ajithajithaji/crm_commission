# -*- coding: utf-8 -*-
from odoo import api, fields, models


class SaleOrder(models.Model):
    """Here inherit the model sale order and add new field"""
    _inherit = 'sale.order'

    crm_commission_id = fields.Many2one('crm.commission',
                                        string='Commission Plan',
                                        compute='_compute_commission_plan')
    commission_total = fields.Float(string='Commission Total',
                                    compute='_compute_commission')

    @api.depends('crm_commission_id', 'order_line')
    def _compute_commission(self):
        """This is used to calculate commission"""
        total = 0
        commission_Amount = 0
        for record in self.order_line:
            total += record.price_subtotal
            if self.crm_commission_id.commission_type == 'product_wise':
                for rec in self.crm_commission_id.product_wise_ids:
                    rate = 0
                    if rec.product_id.id == record.product_id.id:
                        rate += (rec.rate_percentage *
                                 record.price_subtotal / 100)
                        if (rec.max_commission_amount and
                                rate > rec.max_commission_amount):
                            commission_Amount += rec.max_commission_amount
                        else:
                            commission_Amount += rate
            elif self.crm_commission_id.revenue_type == 'straight':
                rate = self.crm_commission_id.revenue_wise_ids.rate
                commission_Amount = total * rate / 100
        if self.crm_commission_id.revenue_type == 'graduated':
            amount = total
            for line in self.crm_commission_id.revenue_wise_ids:
                if total > line.from_amount:
                    if amount > line.to_amount:
                        rate = line.to_amount * line.rate / 100
                        amount -= line.to_amount
                        commission_Amount += rate
                    else:
                        rate = amount * line.rate / 100
                        commission_Amount += rate
        self.commission_total = commission_Amount

    @api.depends('user_id', 'team_id')
    def _compute_commission_plan(self):
        for order in self:
            if order.user_id and order.user_id.crm_commission_id:
                order.crm_commission_id = order.user_id.crm_commission_id
            else:
                order.crm_commission_id = order.team_id.crm_commission_id
