# -*- coding: utf-8 -*-
{
    'name': "Taller",

    'summary':"Short alexitop (1 phrase/line) summary of the module's purpose, used as subtitle on modules listing or apps.openerp.com",

    'description': "Longof module's purpose",

    'author': "RobertoT",
    'website': "https://www.github.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Administration',
    'version': '1.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/marca.xml',
        'views/modelo.xml',
        'views/certificado_emisiones.xml',
        'views/normativa.xml',
        'views/vehiculo.xml',
        'views/owner.xml',
        'views/update.xml',
        'views/menus.xml',

    ],
    'application': True,
    'images': ['static/description/logo.png',],
    
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'taller/static/src/scss/style.scss',
        ],
    },
}
