.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
   :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
   :alt: License: AGPL-3

=============================
Partner Data Privacy Consent
=============================

This module provides the master data foundation for partner data privacy
consent management:

* **Consent Purpose** (``partner_consent_purpose``) - the list of specific
  purposes for which personal data may be processed.
* **Privacy Notice** (``partner_consent_notice``) - versioned privacy notice
  documents whose exact agreed text is stored per version, together with the
  purposes they cover.

Both master data are available under *Contacts -> Configuration -> Data
Privacy* and are meant to be referenced by partner consent records.


Work Instruction
================

* `Consent Purpose <docs/partner_consent_purpose/index.html>`_
* `Privacy Notice <docs/partner_consent_notice/index.html>`_


Installation
============

To install this module, you need to:

1.  Clone the branch 14.0 of the repository https://github.com/open-synergy/ssi-partner
2.  Add the path to this repository in your configuration (addons-path)
3.  Update the module list
4.  Go to menu *Apps -> Apps -> Main Apps*
5.  Search For *Partner Data Privacy Consent*
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

* Andhitia Rama <andhitia.r@gmail.com>

Maintainer
----------

.. image:: https://simetri-sinergi.id/logo.png
   :alt: PT. Simetri Sinergi Indonesia
   :target: https://simetri-sinergi.id.com

This module is maintained by the PT. Simetri Sinergi Indonesia.
