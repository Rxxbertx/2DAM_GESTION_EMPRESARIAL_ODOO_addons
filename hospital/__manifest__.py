# -*- coding: utf-8 -*-
{
    'name': "hospital",

    'summary': "hospital",

    'description': """
hospital
    """,

    'author': "Alexis&Roberto",
    'website': "https://github.com/Rxxbertx",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '1.0',
    'installable': True,
    'application': True,
    'auto_install': False,

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/menu.xml',
        'views/Doctor.xml',
    ],
}
