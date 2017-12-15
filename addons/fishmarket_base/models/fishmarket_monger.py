# -*- coding: utf-8 -*-
from odoo import models, fields, api

class MongerBase(models.Model):

    _name = 'fishmarket.monger'

    name = fields.Char(string='魚販名稱')
    code = fields.Char(string='魚販代號')
    # debt_date = fields.Date(string='欠款日期(是否拔除 欠款黨有日期)')
    debt_amount = fields.Integer(string='總欠金額',compute='setdebtamount')
    after_amount = fields.Integer(string='餘欠金額',compute='setmoney')
    belongs = fields.Char(string='屬')
    ps = fields.Char(string='備註')
    print1 = fields.Boolean(string='印單')

    monger_debt = fields.One2many(comodel_name='monger.debt',inverse_name='name',string='欠錢不還')
    monger_income = fields.One2many(comodel_name='fishmarket.monger.income',inverse_name='monger_name',string='還錢棒棒')

    @api.depends('monger_debt')
    def setdebtamount(self):
        for row in self:
            for line in row.monger_debt:
                    row.debt_amount += line.debt_amount
            #line.debt_amount = line.monger_debt.name.total_owe_money
    @api.depends('monger_income')
    def setmoney(self):
        income_total = 0
        for row in self:
                row.after_amount = row.debt_amount
        for row in self:
            for line in row.monger_income:
                income_total += line.record_money
                row.after_amount = row.debt_amount - income_total


class MongerPrintWizard(models.Model):
    _name = 'monger.print.wizard'

    name = fields.Char()

    monger = fields.Many2many(comodel_name='fishmarket.monger', string='欲列印魚販名稱')

    def printmongerwizard(self):
        Report = self.env['report']
        monger = self.monger
        data={
            'monger': monger.ids,
        }
        return Report.get_action([],
            'fishmarket_base.monger_template', data)
