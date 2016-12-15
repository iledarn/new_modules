# -*- coding: utf-8 -*-
from openerp import fields, models, api
from openerp.addons.connector.connector import Environment
from openerp.addons.connector.checkpoint import checkpoint


class NadaBinding(models.AbstractModel):
    _name = 'nada.binding'
    _inherit = 'external.binding'
    _description = 'Nada Binding (abstract)'

    # 'openerp_id': openerp-side id must be declared in concrete model
    backend_id = fields.Many2one(
        comodel_name='nada.backend',
        string='Nada Backend',
        required=True,
        ondelete='restrict',
    )
    # fields.char because 0 is a valid coffee ID
    nada_ID = fields.Char(string='ID in the Nada System',
                            select=True)


def get_environment(session, model_name, backend_id):
    """ Create an environment to work with. """
    backend_record = session.env['nada.backend'].browse(backend_id)
    env = Environment(backend_record, session, model_name)
    lang = backend_record.default_lang_id
    lang_code = lang.code if lang else 'en_US'
    if lang_code == session.context.get('lang'):
        return env
    else:
        with env.session.change_context(lang=lang_code):
            return env


def add_checkpoint(session, model_name, record_id, backend_id):
    return checkpoint.add_checkpoint(session, model_name, record_id,
                                     'nada.backend', backend_id)
