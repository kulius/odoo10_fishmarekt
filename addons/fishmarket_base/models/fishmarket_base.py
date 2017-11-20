# -*- coding: utf-8 -*-
from odoo import models, fields, api

class BaseBase(models.Model):
    _name = 'fishmarket.base'

    cage_deposit_amount = fields.Integer(string='塑膠籠押金金額')
    summons_amount = fields.Integer(string='每張傳票金額')
    sales_profit = fields.Float(string='銷貨毛利')
