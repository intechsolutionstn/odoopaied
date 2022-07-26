# -*- coding: utf-8 -*-
{
    'name': "Incoming Payments - Check ",

    'summary': """
       Imprission de certificat de retenue à la source""",
    'description': """
        Model de Incoming Payments  Check
    """,
    'author': "",
    'website': "",
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
    "price": 30,
    "currency": 'EUR',
    'images': ['static/description/bank.jpg'],
}
