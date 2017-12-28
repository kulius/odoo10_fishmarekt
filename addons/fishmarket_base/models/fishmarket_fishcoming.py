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

     #魚貨來源
class WhereFish(models.Model):
    _name = 'where.fish'

    name = fields.Char(string='魚貨來源')


    #魚販過帳作業
class MongerPostingWizard(models.Model):
    _name = 'monger.posting.wizard'

    set_the_price = fields.Boolean(string='要計算了嗎？')
    posting_date = fields.Date(string='過帳日期',compute='set_date')

    name = fields.Many2one(comodel_name='fishmarket.monger',string='欲過帳之魚販')
    last_debt = fields.Integer(string='前日欠' ,compute='set_posting')
    income = fields.Integer(string='入金', compute='set_posting')
    today_debt = fields.Integer(string='本日欠', compute='settodaydebt')



    # 過帳後的資料
    last_debt2 = fields.Integer(string='前日欠',compute='set_income')
    income1 = fields.Integer(string='入金',compute='set_income')
    sell_total = fields.Integer(string='賣總價', compute='set_posting')
    posting_today_debt = fields.Integer(string='過帳後本日欠', compute='set_posting_today_debt')

    relation = fields.Many2many(comodel_name='fishmarket.monger.sale',string='魚販到傳票')

    @api.depends('set_the_price')
    def set_date(self):
        setting = self.env['fishmarket.set'].search([])
        for line in setting:
            self.posting_date = line.working_date


    @api.depends('set_the_price')
    def set_posting(self):
            #計算賣總和
        monger_summoms = self.env['fishmarket.monger.sale'].search([('now_status', '=', 1)])
        debt = self.env['monger.debt']
        self.sell_total = 0
        for line in monger_summoms:
            self.name = line.name
            self.sell_total += line.sell_total

            #計算入金
        monger_income = self.env['fishmarket.monger.income'].search([('now_status', '=', 1)])
        self.income = 0
        for line in monger_income:
            self.income +=line.record_money

            #計算前欠金額
        monger_debt = self.env['fishmarket.monger'].search([])
        self.last_debt = 0
        for line in monger_debt:
            self.last_debt += line.debt_amount

            #過帳紀錄 -->欠款黨新增欠款紀錄
    def create_debt(self):
        monger_summoms = self.env['fishmarket.monger.sale'].search([('now_status', '=', 1)])
        debt = self.env['monger.debt']
        self.sell_total = 0
        time = int(fields.datetime.now().strftime("%m%d") + u"00")
        for line in monger_summoms:
            code = u'ABC' + str(time)
            self.name = line.name
            self.sell_total += line.sell_total
            line.now_status = 2
            debt.create({
                'debt_code': code,
                'name': self.name.id,
                'date': self.posting_date,
                'debt_amount': line.sell_total,
            })
            time +=1

            #更改入金的狀態
        monger_income = self.env['fishmarket.monger.income'].search([('now_status', '=', 1)])
        for line in monger_income:
            line.now_status = 2



    @api.depends('last_debt','income')
    def settodaydebt(self):
        self.today_debt = self.last_debt - self.income


    @api.onchange('income')
    def set_income(self):
        self.income1 = self.income
        self.last_debt2 =self.last_debt

    #過帳後本日欠
    @api.depends('last_debt2','income1','sell_total')
    def set_posting_today_debt(self):
        self.posting_today_debt = self.last_debt2 - self.income1 + self.sell_total


    # def set_last_debt(self):
    #     last_debt = self.env['fishmarket.monger'].search([])
    #     self.sell_total = 0
    #     for line in last_debt:
    #         self.sell_total += line.after_amount
    #         print self.sell_total

    # @api.onchange('name')
    # def set_sell_total(self):
    #     for row in self:
    #         for line in row.relation:
    #             row.sell_total += line.sell_total