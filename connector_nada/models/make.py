# -*- coding: utf-8 -*-

from odoo import fields, models, api
from odoo.addons.connector.unit.mapper import ExportMapChild, ImportMapChild, ImportMapper, mapping


class ConnectorNadaMake(models.Model):
    _name = 'connector_nada.nada.make'
    _inherit = 'nada.binding'
    _inherits = {'nada.make': 'odoo_make_id'}
    _description = 'Nada Connector Make'

    odoo_make_id = fields.Many2one(
        comodel_name='nada.make',
        string='Make',
        required=True,
        ondelete='restrict',
    )
    nada_make_id = fields.Integer()


@nada
class MakeImportMapper(ImportMapper):
    _model_name = ['connector_nada.nada.make']
    _map_child_class = OdooImportMapChild
