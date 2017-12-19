# -*- coding: utf-8 -*-
from odoo import models, fields, api

class FishBase(models.Model):

    _name = 'fishmarket.fish'

    code = fields.Char(string='魚種代號')
    name = fields.Char(string='魚種名稱')
    ps = fields.Text(string='備註')

    @api.model
    def name_search(self, name='', args=None, operator='ilike', limit=100):
        args = args or []
        domain = []
        if name:
            domain = ['|', ('name', operator, name), ('code', operator, name)]
        banks = self.search(domain + args, limit=limit)
        return banks.name_get()



class FishPrintWizard(models.Model):
    _name = 'fish.print.wizard'

    name = fields.Char()
    fish = fields.Many2many(comodel_name='fishmarket.fish',string='欲列印魚種名稱')


    def fishprintwizard(self):
        Report = self.env['report']
        docs = self.fish
        data = {
                  'docs': docs.ids,
             }

        return Report.get_action([],
            'fishmarket_base.fish_template', data)


class UndoAction(models.Model):
    _name = 'undo.action'

class doAction(models.Model):
    _name = 'do.action'


