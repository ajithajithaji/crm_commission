# -*- coding: utf-8 -*-
from odoo import fields, models


class CrmTeamMember(models.Model):
    """Inherit a model and add new field in salesperson"""
    _inherit = 'crm.team.member'

    crm_commission_id = fields.Many2one('crm.commission',
                                        string='Commission Plan')
