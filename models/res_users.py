# -*- coding: utf-8 -*-
from odoo import fields, models


class ResUsers(models.Model):
    _inherit = 'res.users'

    crm_commission_id = fields.Many2one('crm.commission',
                                        string='Commission Plan')
