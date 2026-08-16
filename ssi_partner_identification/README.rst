.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
   :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
   :alt: License: AGPL-3

======================
Partner Identification
======================

This module adds a dedicated **Identities** menu (Contacts > Configuration >
Identities) and its own security groups for the ``res.partner.id_category`` and
``res.partner.id_number`` models provided by the OCA module ``partner_identification``.

**Models:**

* **Partner ID Category** (``res.partner.id_category``, from ``partner_identification``)
  — a type of identification document, e.g. "Driver License".
* **Partner ID Number** (``res.partner.id_number``, from ``partner_identification``) —
  an identification number issued to a partner.

Work Instruction
================

* `Create Partner ID Category <docs/res_partner_id_category/01-create.html>`_
* `Edit Partner ID Category <docs/res_partner_id_category/02-edit.html>`_
* `Delete Partner ID Category <docs/res_partner_id_category/03-delete.html>`_
* `Deactivate Partner ID Category <docs/res_partner_id_category/04-deactivate.html>`_
* `Activate Partner ID Category <docs/res_partner_id_category/05-activate.html>`_
* `Create Partner ID Number <docs/res_partner_id_number/01-create.html>`_
* `Edit Partner ID Number <docs/res_partner_id_number/02-edit.html>`_
* `Delete Partner ID Number <docs/res_partner_id_number/03-delete.html>`_
* `Deactivate Partner ID Number <docs/res_partner_id_number/04-deactivate.html>`_
* `Activate Partner ID Number <docs/res_partner_id_number/05-activate.html>`_

Installation
============

To install this module, you need to:

1.  Clone the branch 14.0 of the repository https://github.com/open-synergy/ssi-partner
2.  Add the path to this repository in your configuration (addons-path)
3.  Update the module list
4.  Go to menu *Apps -> Apps -> Main Apps*
5.  Search For *Partner Identification*
6.  Install the module

Bug Tracker
===========

Bugs are tracked on `GitHub Issues
<https://github.com/open-synergy/ssi-partner/issues>`_.
In case of trouble, please check there if your issue has already been reported.
If you spotted it first, help us smashing it by providing a detailed
and welcomed feedback.


Credits
=======

Contributors
------------

* Michael Viriyananda <viriyananda.michael@gmail.com>

Maintainer
----------

.. image:: https://simetri-sinergi.id/logo.png
   :alt: PT. Simetri Sinergi Indonesia
   :target: https://simetri-sinergi.id

This module is maintained by the PT. Simetri Sinergi Indonesia.
