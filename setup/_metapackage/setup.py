import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo14-addons-open-synergy-ssi-partner",
    description="Meta package for open-synergy-ssi-partner Odoo addons",
    version=version,
    install_requires=[
        'odoo14-addon-ssi_partner',
        'odoo14-addon-ssi_partner_education_level',
        'odoo14-addon-ssi_partner_experience',
        'odoo14-addon-ssi_partner_identification',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
        'Framework :: Odoo :: 14.0',
    ]
)