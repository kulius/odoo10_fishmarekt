# -*- coding: utf-8 -*-
from odoo import models, fields, api

class SummomsStatisic(models.Model):
    _name = 'fishmarket.summoms.statisic'

    name = fields.Char()
    monger_order = fields.Char(string='件')
    cage = fields.Intege    r(string='籠')
    total_weight = fields.Float(string='總重量')
    buy_total = fields.Float(string='')
