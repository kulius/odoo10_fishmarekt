# -*- coding: utf-8 -*-
from odoo import models, fields, api

#傳票統計的資料存在魚貨來源 方便各個來源做資料查詢和運算
class FishComing(models.Model):

    _name = 'fish.coming'

    write_date = fields.Date(string='寫入時間')
    name = fields.Many2one(comodel_name='where.fish',string='魚貨來源')
    order = fields.Integer(string='件', store = True)
    cage = fields.Integer(string='籠')
    weight_total = fields.Float(string='總重量',compute = 'compute_total_weight' ,store = True)
    buy_total = fields.Integer(string='買總價', compute = 'compute_buy_total',store = True)
    sell_total = fields.Integer(string='賣總價',compute = 'compute_sell_total',store = True)
    surplus = fields.Integer(string='盈餘', compute='setsurplus' , store=True)
    # loss = fields.Float(string='虧損')

    relation = fields.Many2many(comodel_name='fishmarket.monger.sale',string='關聯')

    @api.onchange('relation')
    def setorder(self):
        relation = self.relation
        count_order = 0
        for line in relation:
            count_order += 1
            self.order = count_order


    @api.depends('buy_total','sell_total')
    def setsurplus(self):
        for line in self:
            line.surplus  = line.sell_total - line.buy_total

    @api.depends('relation.sell_total')
    def compute_sell_total(self):
        for row in self:
            for line in row.relation:
                row.sell_total += line.sell_total

    @api.depends('relation.buy_total')
    def compute_buy_total(self):
        for row in self:
            for line in row.relation:
                row.buy_total += line.buy_total

    @api.depends('relation.sell_weight')
    def compute_total_weight(self):
        for row in self:
            for line in row.relation:
                row.weight_total += line.sell_weight


                    #
    # def setweight(self):
    #     for line in self.env['fishmarket.monger.sale']:
    #         self.weight_total += line.buy_weight
    #         self.buy_total += line.buy_total
    #


class WhereFish(models.Model):
    _name = 'where.fish'

    name = fields.Char(string='魚貨來源')
