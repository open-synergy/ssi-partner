from odoo import models


class ResPartnerEthnicity(models.Model):
    """Master data listing the ethnicities selectable on a contact.

    Selected on individual ``res.partner`` records to record the
    ethnicity of the person, e.g. for demographic or reporting purposes.
    """

    _name = "res_partner_ethnicity"
    _inherit = [
        "mixin.master_data",
    ]
    _description = "Ethnicity"
