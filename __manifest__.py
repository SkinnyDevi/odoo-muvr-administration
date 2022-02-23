# -*- coding: utf-8 -*-
{
    'name': "Gestion Clipmetrajes",

    'summary': """
        Aplicacion para gestionar clipmetrajes de Manos Unidas""",

    'description': """
        Gestion de valoraciones y clipmetrajes del proyecto de cortos de Manos Unidas.
    """,

    'author': "SkinnyDevi",
    'website': "https://github.com/SkinnyDevi",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Services',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'mail', 'project'],

    # always loaded
    'data': [
        'views/views.xml',
        'views/templates.xml',
        'security/security.xml',
        'security/ir.model.access.csv',
        'reports/clipmetrajes_report.xml',
        'reports/clipmetrajes_report_view.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application': 'True'
}
