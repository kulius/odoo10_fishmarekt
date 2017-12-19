# -*- coding: utf-8 -*-
from odoo import models, fields, api

class MongerIncome(models.Model):

    _name = 'fishmarket.monger.income'

    write_date = fields.Date(string='寫入時間')
    monger_id = fields.Char(string='魚販代號')
    monger_name = fields.Many2one(comodel_name='fishmarket.monger',string='魚販名稱')
    monger_time = fields.Integer(string='次')
    last_owe_money = fields.Integer(string='前欠金額')
    record_money = fields.Integer(string='入金金額')
    total_owe_money = fields.Integer(string='欠餘金額?? 可以拔掉', compute='settotalowemoney', store=True)
    income_date = fields.Date(string='入金時間')

    @api.depends('last_owe_money','record_money')
    def settotalowemoney(self):
        for line in self:
            line.total_owe_money = line.last_owe_money - line.record_money

    @api.onchange('monger_name')
    def setmonger(self):
            self.monger_id = self.monger_name.code
            self.last_owe_money = self.monger_name.debt_amount

class MongerIncomePrintWizard(models.Model):

    _name = 'monger.income.print.wizard'

    relation = fields.Many2many(comodel_name='fishmarket.monger.income',string='欲列印入金資料')

    def setincomewizard(self):
        Report = self.env['report']
        relation = self.relation
        data = {
            'monger_income': relation.ids,
        }
        return Report.get_action([],
                                 'fishmarket_base.monger_income_template', data)


