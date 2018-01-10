# -*- coding: utf-8 -*-
from odoo import models, fields, api

class MongerDebt(models.Model):
    _name = 'monger.debt'

    debt_code = fields.Char(string='代號',readonly=True)
    name = fields.Many2one(comodel_name='fishmarket.monger',string='魚販名稱')
    date = fields.Date(string='欠款日期', readonly=True, compute='set_date' )
    debt_amount = fields.Integer(string='欠款金額' )


    debt_order = fields.One2many(comodel_name='fishmarket.monger.income',inverse_name='monger_name',string='還錢明細表')

    @api.depends('name')
    def set_date(self):
        setting = self.env['app.theme.config.settings'].search([])
        for line in setting:
            self.date = line.working_date

    @api.model
    def create(self, vals):
        res_id = super(MongerDebt, self).create(vals)
        time = fields.datetime.now().strftime("%m%d"+u'00') + str(res_id.id)
        code = u'REQ' + time
        #寫入變數res_id
        res_id.write({
          'debt_code': code,
        })
        return res_id

    @api.multi
    def write(self, vals):
        # 函式複寫，並回傳res_id
        res_id = super(MongerDebt, self).write(vals)
        return res_id



