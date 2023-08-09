# -*- coding: utf-8 -*-
from odoo import fields, models


class CrmTeam(models.Model):
    """Inherit model crmTeam and add new field in SalesTeam"""
    _inherit = 'crm.team'

    crm_commission_id = fields.Many2one('crm.commission',
                                        string='Commission Plan')
