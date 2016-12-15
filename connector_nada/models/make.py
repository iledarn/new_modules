# -*- coding: utf-8 -*-

from odoo import fields, models, api


class ConnectorNadaMake(models.Model):
    _name = 'connector_nada.nada.make'
    _inherit = 'nada.binding'
    _inherits = {'nada.make': 'odoo_id'}
    _description = 'Nada Connector Make'

    odoo_id = fields.Many2one(
        comodel_name='nada.make',
        string='Make',
        required=True,
        ondelete='restrict',
    )
