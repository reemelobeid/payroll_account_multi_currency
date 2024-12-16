# -*- coding:utf-8 -*-

from collections import defaultdict
from markupsafe import Markup

from odoo import fields, models, _, api
from odoo.exceptions import UserError, ValidationError
from odoo.tools import float_compare, float_is_zero, plaintext2html

class HrPayslip(models.Model):
    _inherit = 'hr.payslip'

    currency_id = fields.Many2one("res.currency", related='', string="Currency")

    @api.onchange('contract_id')
    def onchange_contract_id(self):
        self.currency_id = self.contract_id.currency_id

    def _prepare_line_values(self, line, account_id, date, debit, credit):
        res = super(HrPayslip, self)._prepare_line_values(line, account_id, date, debit, credit)
        is_foreign_currency = self.currency_id != self.company_id.currency_id
        if is_foreign_currency:
            currency_id = self.currency_id
            res.update({
                "currency_id": currency_id.id,
            })
            if debit != 0.0:
                amount_currency = debit
                debit = currency_id.with_context(dict(self._context))._convert(debit, self.company_id.currency_id)  # amount converted to base company currency
                res.update({
                    "debit": debit,
                    "amount_currency": amount_currency,
                })
            if credit != 0.0:
                amount_currency = credit
                credit = currency_id.with_context(dict(self._context))._convert(credit, self.company_id.currency_id)  # amount converted to base company currency
                res.update({
                    "credit": credit,
                    "amount_currency": - amount_currency,
                })
        return res

