# Copyright 2024 OpenSynergy Indonesia
# Copyright 2024 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import base64
import functools
import json
import logging
import math
import re

from werkzeug import urls
from odoo import fields as odoo_fields, http, tools, _, SUPERUSER_ID
from odoo.exceptions import ValidationError, AccessError, MissingError, UserError, AccessDenied
from odoo.http import content_disposition, Controller, request, route
from odoo.tools import consteq
from odoo.addons.portal.controllers import portal
from odoo.addons.portal.controllers.portal import CustomerPortal

_logger = logging.getLogger(__name__)


class CustomerPortalExtended(CustomerPortal):

    @route('/my/identifications', type='http', auth='user', website=True, methods=['GET', 'POST'])
    def identifications(self, **post):
        values = self._prepare_portal_layout_values()
        values['get_error'] = portal.get_error
        values['id_numbers'] = request.env.user.partner_id.id_numbers

        return request.render('ssi_partner_identification_portal.portal_my_identifications', values, headers={
            'X-Frame-Options': 'DENY'
        })
