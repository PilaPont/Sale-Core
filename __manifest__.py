{
    'name': 'Sale Core',
    'version': '14.0.0.1.0.0+210609',
    'description': """
    This module converts original sale demo and data records into Farsi.
    """,
    'author': "Kenevist Developers, Maryam Kia",
    'website': "https://www.kenevist.ir",
    'license': 'OPL-1',
    'category': 'Localization',

    'depends': ['sale'],
    'data': [
        'data/ir_sequence_data.xml',
    ],
    'demo': [
        'data/sale_demo.xml',
    ],

    'auto_install': True,
    'application': False,
    'installable': True,
}
