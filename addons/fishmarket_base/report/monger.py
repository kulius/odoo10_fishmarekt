# -*- coding: utf-8 -*-
from odoo import models, fields, api

class ReportMonger(models.AbstractModel):
    _name = 'report.fishmarket_base.monger_template'

    name = fields.Char()

    @api.model
    def render_html(self, docids ,data=None):
        Report = self.env['report']
        x = data['monger']
        doc = self.env['fishmarket.monger'].browse(x)
        docargs = {
            'doc_ids': docids,
            'doc_model': 'fishmarket_base.monger_template',
            'docs': doc,
        }
        return Report.render('fishmarket_base.monger_template', docargs)
