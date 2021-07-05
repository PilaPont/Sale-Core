{
    'name': 'Sale Core',
    'version': '14.0.0.1.2.0+210705',
    'description': """
     This module modifies some properties of Sale, including:
    - Converts original Sale demo and data records into Farsi
    - monetary widget for price_unit
    - add unit column to optional products
    """,
    'author': "Kenevist Developers, Maryam Kia",
    'website': "https://www.kenevist.ir",
    'license': 'OPL-1',
    'category': 'Localization',

    'depends': ['sale','sale_management'],
    'data': [
        'data/ir_sequence_data.xml',
        'views/sale_views.xml',
        'views/sale_order_views.xml',
        'report/sale_report_templates.xml',
    ],
    'demo': [
        'data/sale_demo.xml',
    ],

    'auto_install': True,
    'application': False,
    'installable': True,
}
