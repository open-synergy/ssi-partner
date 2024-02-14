# Copyright 2023 OpenSynergy Indonesia
# Copyright 2023 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo.addons.portal.controllers.portal import CustomerPortal
from odoo.http import content_disposition, Controller, request, route
from odoo.addons.portal.controllers import portal

CustomerPortal.OPTIONAL_BILLING_FIELDS.append('mobile')


class CustomerPortalExtended(CustomerPortal):

    @route(
        ['/my/bank_accounts'],
        type='http',
        auth='user',
        website=True,
        methods=['GET']
    )
    def bank_accounts(self):
        values = self._prepare_portal_layout_values()
        values['get_error'] = portal.get_error
        values['bank_account_ids'] = request.env['portal_partner_bank_account'].search([
            ('partner_id', '=', request.env.user.partner_id.id)
        ])

        return request.render('ssi_partner_portal.portal_my_bank_accounts', values, headers={
            'X-Frame-Options': 'DENY'
        })

    @route(
        ['/my/bank_account', '/my/bank_account/<int:id>'],
        type='http',
        auth='user',
        website=True,
        methods=['GET', 'POST']
    )
    def bank_account(self, **post):
        id = post.get('id')
        bank_account_obj = request.env['portal_partner_bank_account']
        bank_obj = request.env['res.bank'].sudo()
        currency_obj = request.env['res.currency'].sudo()
        values = self._prepare_portal_layout_values()
        error_messages = []
        values.update({
            'error_message': '',
            'bank_ids': bank_obj.search([]),
            'currency_ids': currency_obj.search([]),
            'current_bank_account_id': bank_account_obj,
        })
        current_bank_account_id = bank_account_obj
        if id:
            id = int(id)
            current_bank_account_id = bank_account_obj.search([
                ('id', '=', id)
            ])
            values.update({
                'current_bank_account_id': current_bank_account_id,
            })

        if request.httprequest.method == 'POST':
            bank_account_vals = {
                'partner_id': request.env.user.partner_id.id,
                'acc_number': post.get('acc_number'),
                'acc_holder_name': post.get('acc_holder_name'),
            }
            if post.get('bank'):
                bank_id = bank_obj.sudo().search([
                    ('id', '=', int(post.get('bank', '0')))
                ])
                if not bank_id:
                    error_messages.append('Bank not found.')
                bank_account_vals.update({
                    'bank_id': bank_id.id,
                })
            if post.get('currency'):
                currency_id = currency_obj.sudo().search([
                    ('id', '=', int(post.get('currency', '0')))
                ])
                if not currency_id:
                    error_messages.append('Currency not found.')
                bank_account_vals.update({
                    'currency_id': currency_id.id,
                })
            if error_messages:
                values['error_message'] = '\n'.join(error_messages)
                return request.render('ssi_partner_portal.portal_my_bank_account', values, headers={
                    'X-Frame-Options': 'DENY'
                })
            if not current_bank_account_id:
                bank_account_obj.create(bank_account_vals)
            else:
                current_bank_account_id.write(bank_account_vals)
            return request.redirect('/my/bank_accounts')

        return request.render('ssi_partner_portal.portal_my_bank_account', values, headers={
            'X-Frame-Options': 'DENY'
        })

    @route(
        ['/my/bank_account/remove/<int:id>'],
        type='http',
        auth='user',
        website=True,
        methods=['GET', 'POST']
    )
    def remove_bank_account(self, **post):
        id = post.get('id')
        bank_account_id = request.env['portal_partner_bank_account'].search([
            ('id', '=', int(id))
        ])
        bank_account_id.unlink()
        return request.redirect('/my/bank_accounts')
