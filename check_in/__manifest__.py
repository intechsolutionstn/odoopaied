# -*- coding: utf-8 -*-
{
    'name': "Incoming Payments - Check ",

    'summary': """
       this module allows you to tick the incoming check payment in odoo payment""",
    'description': """
        Model de Incoming Payments  Check
    """,
    'author': "InTech Solutions",
    'website': "www.intech-eg.tech",
    'category': 'accounting',
    'version': '1.2.0',
    'depends': ['account',
                'account_check_printing'
                ],
    'data': [
        # 'security/ir.model.access.csv',
        'data/account_check_data.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
    'license': 'OPL-1',
    "price": 10,
    "currency": 'EUR',
    'images': ['static/description/bank.jpg'],
}
