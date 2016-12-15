# -*- coding: utf-8 -*-

from odoo import models, fields, api

class NadaVersion(models.Model):
    _name = 'nada.version'

    name = fields.Char()


class NadaMakeName(models.Model):
    _name = 'nada.make_template'

    name = fields.Char()


class NadaCategory(models.Model):
    _name = 'nada.category'

    name = fields.Char()


class NadaMake(models.Model):
    _name = 'nada.make'
    _inherits = {
        'nada.make_template': 'make_template_id',
        'nada.version': 'version_id',
        'nada.category': 'category_id'
    }

    make_template_id = fields.Many2one('nada.make_template')
    category_id = fields.Many2one('nada.category')
    version_id = fields.Many2one('nada.version')
