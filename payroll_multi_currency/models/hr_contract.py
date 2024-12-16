# -*- coding:utf-8 -*-
from dateutil.relativedelta import relativedelta
from odoo import api, fields, models, _

class HrContract(models.Model):
    _inherit = 'hr.contract'
    _description = 'Employee Contract'

    currency_id = fields.Many2one("res.currency", string="Currency", readonly=False,
                                  related='', store=True, default=lambda self: self.env.company.currency_id)
