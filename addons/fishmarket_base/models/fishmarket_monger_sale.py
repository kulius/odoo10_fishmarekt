# -*- coding: utf-8 -*-
from odoo import models, fields, api

class MongerSaleSummoms(models.Model):
    _name = 'fishmarket.monger.sale'

    total_order = fields.Char(string='件數')
    monger_id = fields.Char(string='魚販代號')
    monger_name = fields.Many2one(comodel_name='fishmarket.monger',string='魚販名稱',required=True)
    monger_order = fields.Integer(string='件數')
    buy_weight = fields.Float(string='買重')
    buy_dollar = fields.Float(string='買價')
    buy_total = fields.Float(string='買總價')

    fish_id = fields.Char(string='魚種代號')
    fish_name = fields.Many2one(comodel_name='fishmarket.fish',string='魚種名稱',required=True)
    cage = fields.Integer(string='籠數')
    sell_weight = fields.Float(string='賣重')
    sell_dollar = fields.Float(string='賣價')
    sell_total = fields.Float(string='賣總價')
    count_bonus = fields.Float(string='加成')

    fish_come = fields.Selection(selection=[(1,'魚市',),(2,'在庫'),(3,'自己')],string='魚貨來源')
    write_date = fields.Date(string='寫入時間')

    @api.onchange('monger_name')
    def setmonger(self):
        self.monger_id = self.monger_name.monger_id

    @api.onchange('fish_name')
    def setfish(self):
        self.fish_id = self.fish_name.fish_id