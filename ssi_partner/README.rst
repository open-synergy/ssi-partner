.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
   :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
   :alt: License: AGPL-3

=======
Partner
=======

Foundation module for SSI partner-related customizations. Provides the
``Partner`` application menu, five master data models used across SSI
implementations (``company_ownership_type``, ``company_entity_type``,
``res_partner_religion``, ``res_partner_ethnicity``,
``res_partner_bank_usage``), and a re-implementation of ``res.partner.title``
(removed from Odoo 19 core). It also adds ``usage_id`` on
``res.partner.bank``, a ``branch`` value on ``res.partner.type``, and the
``action_open_contact_address`` method used to browse a company's child
contacts.

Adds native individual attributes (gender, date/place of birth, computed
age, nationality, blood type, religion, ethnicity, marital status, spouse
information, title) and company attributes (ownership type, entity type,
secondary industries) directly on ``res.partner``, presented on two
mutually exclusive notebook pages depending on ``is_company``. Also adds
the ``partner_contact_group`` master data model, used to group a subset of
a commercial contact's children for handling as a single unit.

Adds a mechanism for a single person to hold several positions across
different companies without being duplicated as unrelated contacts: a
``standalone`` contact can have several ``attached`` positions
(``contact_id``/``other_contact_ids``) whose name and title are kept in
sync with it. Contact lists only show standalone contacts by default; the
"All Positions" filter on the partner search view reveals attached
contacts as well.

Adds a partner identification mechanism: the ``res_partner_id_category``
master data model (National ID, Tax ID, Driving License, Passport,
Business Registration Number, etc.), each optionally carrying a Python
``validation_code`` used to validate the format of numbers assigned to it,
and the ``res_partner_id_number`` model, shown as an "ID Numbers" tab on
``res.partner``, tracking the number, issuing partner, issue date, and
validity period (with a computed Draft/Valid/Expired ``status``).


Installation
============

To install this module, you need to:

1.  Clone the branch 19.0 of the repository https://github.com/open-synergy/ssi-partner
2.  Add the path to this repository in your configuration (addons-path)
3.  Update the module list (Must be on developer mode)
4.  Go to menu *Apps -> Apps -> Main Apps*
5.  Search For *Partner*
6.  Install the module


Bug Tracker
===========

Bugs are tracked on `GitHub Issues
<https://github.com/open-synergy/ssi-partner/issues>`_. In case of trouble, please
check there if your issue has already been reported. If you spotted it first,
help us smash it by providing detailed and welcomed feedback.


Credits
=======

Contributors
------------

* Andhitia Rama <andhitia.r@gmail.com>

Maintainer
----------

.. image:: https://simetri-sinergi.id/logo.png
   :alt: PT. Simetri Sinergi Indonesia
   :target: https://simetri-sinergi.id

This module is maintained by the PT. Simetri Sinergi Indonesia.
