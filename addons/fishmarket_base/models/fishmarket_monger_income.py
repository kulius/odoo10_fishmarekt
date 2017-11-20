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
    total_owe_money = fields.Integer(string='欠餘金額')


    @api.onchange('monger_name')
    def setmonger(self):
        self.monger_id = self.monger_name.monger_id
        self.last_owe_money = self.monger_name.debt_amount