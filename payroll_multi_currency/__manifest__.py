# -*- coding: utf-8 -*-
{
    'name': 'Payroll Multi Currency',
    'author': 'Reem Elobeid',
    'category': 'Human Resources',
    'version': '1.0.0',
    'description': """Payroll in Multi Currency""",
    'summary': 'Pay your employees in different currencies',
    'sequence': 11,
    'depends': ['base', 'hr', 'hr_contract', 'hr_payroll_account'],
    'price': '20.0',
    'currency': 'USD',
    'license': 'LGPL-3',
    'data': [
        'views/hr_contract_views.xml',
        'views/hr_payslip_views.xml',
    ],
    'images': ['static/description/banner.png'],
}