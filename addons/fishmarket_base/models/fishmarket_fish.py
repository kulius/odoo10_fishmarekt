# -*- coding: utf-8 -*-
from odoo import models, fields, api

class FishBase(models.Model):

    _name = 'fishmarket.fish'

    fish_id = fields.Char(string='魚種代號')
    fish_name = fields.Char(string='魚種名稱')
    fish_ps = fields.Text(string='備註')
    # fish_create = fields.Boolean(string='Y/N')
