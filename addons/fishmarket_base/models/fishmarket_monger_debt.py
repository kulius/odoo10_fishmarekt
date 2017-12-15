# -*- coding: utf-8 -*-
from odoo import models, fields, api

class MongerDebt(models.Model):
    _name = 'monger.debt'

    code = fields.Char(string='代號')
    name = fields.Many2one(comodel_name='fishmarket.monger',string='魚販名稱')
    date = fields.Date(string='欠款日期')
    debt_amount = fields.Integer(string='欠款金額')

    @api.onchange('name')
    def setname(self):
        self.code = self.name.code

    debt_order = fields.One2many(comodel_name='fishmarket.monger.income',inverse_name='monger_name',string='還錢明細表')

