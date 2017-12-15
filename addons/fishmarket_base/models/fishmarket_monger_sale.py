# -*- coding: utf-8 -*-
from odoo import models, fields, api

class MongerSaleSummoms(models.Model):
    _name = 'fishmarket.monger.sale'

    order = fields.Char(string='件號')
    monger_id = fields.Char(string='魚販代號')
    monger_name = fields.Many2one(comodel_name='fishmarket.monger',string='魚販名稱',required=True)
    now_status = fields.Selection([(1,'未過帳'),(2,'已過帳')], string='狀態',default=1,index=True)
    monger_order = fields.Integer(string='件數')
    buy_weight = fields.Float(string='買重(KG)')
    buy_dollar = fields.Float(string='買價(TWD)')
    buy_total = fields.Float(string='買總價',compute='settotalbuy',store=True)

    fish_id = fields.Char(string='魚種代號')
    fish_name = fields.Many2one(comodel_name='fishmarket.fish',string='魚種名稱',required=True)
    cage = fields.Integer(string='籠數')
    sell_weight = fields.Float(string='賣重(KG)')
    sell_dollar = fields.Float(string='賣價(TWD)')
    sell_total = fields.Float(string='賣總價',compute='settotal',store=True)
    count_bonus = fields.Float(string='加成')
    division = fields.Float(string='分割')

    fish_come = fields.Many2one(comodel_name='where.fish',string='魚貨來源')
    write_date = fields.Date(string='寫入時間')
    total_buy = fields.Integer(string='總計買入')
    total_sell = fields.Integer(string='總計賣出')

    @api.onchange('monger_name')
    def setmonger(self):
        self.monger_id = self.monger_name.code

    @api.onchange('fish_name')
    def setfish(self):
        self.fish_id = self.fish_name.code

    @api.depends('sell_weight','sell_dollar')
    def settotal(self):
        for line in self:
            line.sell_total = line.sell_weight * line.sell_dollar

    @api.depends('buy_weight','buy_dollar')
    def settotalbuy(self):
        for line in self:
            line.buy_total = line.buy_weight * line.buy_dollar