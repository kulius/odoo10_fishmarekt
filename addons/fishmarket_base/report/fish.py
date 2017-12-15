# -*- coding: utf-8 -*-
from odoo import models, fields, api

class ReportFish(models.AbstractModel):
    _name = 'report.fishmarket_base.fish_template'

    name = fields.Char()

    @api.model
    def render_html(self, docids ,data=None):
        Report = self.env['report']
        x = data['docs']
        doc = self.env['fishmarket.fish'].browse(x)
        docargs = {
            'doc_ids': docids,
            'doc_model': 'fishmarket_base.monger_template',
            'docs': doc,
        }
        return Report.render('fishmarket_base.fish_template', docargs)
