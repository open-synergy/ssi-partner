from odoo import models


class ResPartnerReligion(models.Model):
    """Master data listing the religions selectable on a contact.

    Selected on individual ``res.partner`` records to record the
    religion of the person, e.g. for demographic or reporting purposes.
    """

    _name = "res_partner_religion"
    _inherit = [
        "mixin.master_data",
    ]
    _description = "Religion"
