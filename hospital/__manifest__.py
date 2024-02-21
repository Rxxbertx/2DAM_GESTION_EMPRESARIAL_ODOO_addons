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
    'depends': ['web', 'base'],

    # always loaded
    'data': [
        'views/Patient.xml',
        'views/Floor.xml',
        'views/Bed.xml',
        'views/doctor.xml',
        'views/Menu.xml',
        #'views/Admission.xml',
        'data/hospital.patient.csv',
        'data/hospital.floor.csv',
        'data/hospital.bed.csv',
        'data/hospital.doctor.csv',
        
    ],
    'assets': {
        'web.assets_backend': [
            'hospital/static/src/scss/menus.scss',
            'hospital/static/src/scss/views.scss',
        ],
    },
}
