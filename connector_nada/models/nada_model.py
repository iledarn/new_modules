# -*- coding: utf-8 -*-
from openerp import fields, models, api


class NadaBackend(models.Model):
    _name = 'nada.backend'
    _description = 'Nada Backend'
    _inherit = 'connector.backend'

    _backend_type = 'nada'

    @api.model
    def _select_versions(self):
        """ Available versions

        Can be inherited to add custom versions.
        """
        return [('2016', 'Version 2016')]

    version = fields.Selection(
        selection='_select_versions',
        string='Version',
        required=True,
    )
    location = fields.Char(string='Location')
    username = fields.Char(string='Username')
    password = fields.Char(string='Password')
    default_lang_id = fields.Many2one(
        comodel_name='res.lang',
        string='Default Language',
    )
