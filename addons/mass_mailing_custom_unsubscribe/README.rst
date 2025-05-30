====================================
Mass mailing unsubscription metadata
====================================

.. 
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
   !! This file is generated by oca-gen-addon-readme !!
   !! changes will be overwritten.                   !!
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
   !! source digest: sha256:d00345dd0b32504bacabadfc5a7b645fd2e29fc08988af57081cbdeba47b2136
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

.. |badge1| image:: https://img.shields.io/badge/maturity-Beta-yellow.png
    :target: https://odoo-community.org/page/development-status
    :alt: Beta
.. |badge2| image:: https://img.shields.io/badge/licence-AGPL--3-blue.png
    :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
    :alt: License: AGPL-3
.. |badge3| image:: https://img.shields.io/badge/github-OCA%2Fmass--mailing-lightgray.png?logo=github
    :target: https://github.com/OCA/mass-mailing/tree/18.0/mass_mailing_custom_unsubscribe
    :alt: OCA/mass-mailing
.. |badge4| image:: https://img.shields.io/badge/weblate-Translate%20me-F47D42.png
    :target: https://translation.odoo-community.org/projects/mass-mailing-18-0/mass-mailing-18-0-mass_mailing_custom_unsubscribe
    :alt: Translate me on Weblate
.. |badge5| image:: https://img.shields.io/badge/runboat-Try%20me-875A7B.png
    :target: https://runboat.odoo-community.org/builds?repo=OCA/mass-mailing&target_branch=18.0
    :alt: Try me on Runboat

|badge1| |badge2| |badge3| |badge4| |badge5|

This addon extends the Odoo subscription engine to provide proof on why
you are sending mass mailings to a given contact, as required by the
GDPR in Europe.

**Table of contents**

.. contents::
   :local:

Usage
=====

Once configured:

1. Go to *Email Marketing > Mailings > Create*.
2. Edit your mass mailing at wish, but remember to add a snippet from
   *Footers*, so people have an *Unsubscribe* link.
3. Send it.
4. If somebody gets unsubscribed, you will see logs about that under
   *Email Marketing > Unsubscriptions*.

Bug Tracker
===========

Bugs are tracked on `GitHub Issues <https://github.com/OCA/mass-mailing/issues>`_.
In case of trouble, please check there if your issue has already been reported.
If you spotted it first, help us to smash it by providing a detailed and welcomed
`feedback <https://github.com/OCA/mass-mailing/issues/new?body=module:%20mass_mailing_custom_unsubscribe%0Aversion:%2018.0%0A%0A**Steps%20to%20reproduce**%0A-%20...%0A%0A**Current%20behavior**%0A%0A**Expected%20behavior**>`_.

Do not contact contributors directly about support or help with technical issues.

Credits
=======

Authors
-------

* Tecnativa

Contributors
------------

- `Tecnativa <https://www.tecnativa.com>`__:

  - Rafael Blasco
  - Antonio Espinosa
  - Jairo Llopis
  - David Vidal
  - Ernesto Tejeda
  - Pedro M. Baeza
  - Carlos Roca
  - Pilar Vargas
  - Carlos Lopez

Maintainers
-----------

This module is maintained by the OCA.

.. image:: https://odoo-community.org/logo.png
   :alt: Odoo Community Association
   :target: https://odoo-community.org

OCA, or the Odoo Community Association, is a nonprofit organization whose
mission is to support the collaborative development of Odoo features and
promote its widespread use.

This module is part of the `OCA/mass-mailing <https://github.com/OCA/mass-mailing/tree/18.0/mass_mailing_custom_unsubscribe>`_ project on GitHub.

You are welcome to contribute. To learn how please visit https://odoo-community.org/page/Contribute.
