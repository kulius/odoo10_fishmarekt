# -*- coding: utf-8 -*-
from odoo import models, fields, api

class MongerBase(models.Model):

    _name = 'fishmarket.monger'

    monger_name = fields.Char(string='魚販名稱')
    monger_id = fields.Char(string='魚販代號')
    debt_date = fields.Date(string='欠款日期')
    debt_amount = fields.Integer(string='欠款金額')
    monger_print = fields.Boolean(string='印單')
    # monger_create = fields.Boolean(string='Y/N')
