# -*- coding: utf-8 -*-
from odoo import models, fields, api

class ReportMongerIncome(models.AbstractModel):
    _name = 'report.fishmarket_base.monger_income_template'

    name = fields.Char()

    @api.model
    def render_html(self, docids ,data=None):
        Report = self.env['report']
        x = data['monger_income']
        doc = self.env['fishmarket.monger.income'].browse(x)
        docargs = {
            'doc_ids': docids,
            'doc_model': 'fishmarket_base.monger_income_template',
            'docs': doc,
        }
        return Report.render('fishmarket_base.monger_income_template', docargs)
