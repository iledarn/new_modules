# -*- coding: utf-8 -*-
import odoo.addons.connector.backend as backend


nada = backend.Backend('nada')
nada2016 = backend.Backend(parent=nada, version='2016')
