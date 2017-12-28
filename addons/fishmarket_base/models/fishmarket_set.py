# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import ValidationError

class FishmarketSet(models.Model):
    _name = 'fishmarket.set'

    name = fields.Char()
    working_date = fields.Date(string='作業日期')

    @api.model
    def create(self, vals):
        res_id = super(FishmarketSet, self).create(vals)
        date_count = self.search([])
        if len(date_count) > 1:
            raise ValidationError('只能處理一天的作業!!')
        return res_id