{
    'name': 'Workshop',
    "license": "LGPL-3",
    'version': "1.0.0",
    'summary': 'General Customization',
    'author': 'Capler',
    'category': 'Customization',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/workshop_actions.xml',
        'views/workshop_view.xml',
        'views/workshop_menu.xml',
    

   ],
    'application': True,
    'installable': True
}