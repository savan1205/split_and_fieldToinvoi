{
    'name': 'sale invoicing',
    'version': '1.0',
    'category': 'sale invoicing',
    'summary': 'sale invoicing',
    'sequence': -600,
    'description': """
This module contains all the common inherted features for sale invoicing.
    """,
    'depends': ['sale','stock'],
    'data':[
        'security/ir.model.access.csv',
        
        'wizard/split_state_wizardView.xml',

        'data/sa_for_Wizard.xml',
        
        'views/sale_order_inheritView.xml',
        'views/so_line_inheritView.xml',
        'views/account_move_inheritView.xml',
    ],
    'demo': [
    ],
    'installable': True,
    'auto_install': False,
    
       
    'license': 'LGPL-3',
}
