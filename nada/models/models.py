# -*- coding: utf-8 -*-

from odoo import models, fields, api

class NadaVersion(models.Model):
    _name = 'nada.version'

    name = fields.Char()


class NadaMakeName(models.Model):
    _name = 'nada.makename'

    name = fields.Char()


class NadaCategory(models.Model):
    _name = 'nada.category'

    name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100


class NadaMake(models.Model):
    _name = 'nada.make'

    name_id = fields.Many2one('nada.makename')
    category_id = fields.Many2one('nada.category')
    version_id = fields.Many2one('nada.version')

