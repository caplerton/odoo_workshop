{
    'name': 'Workshop',
    "license": "LGPL-3",
    'version': "1.0.0",
    'summary': 'General Customization',
    'author': 'Capler',
    'category': 'Customization',
    'depends': ['base', 'website'],
    'data': [
        'security/ir.model.access.csv',
        'views/workshop_actions.xml',
        'views/workshop_view.xml',
        'views/workshop_menu.xml',
        'views/timeslot_view.xml',
        'views/session_view.xml',
        'views/calendar_view.xml',
        'views/workshop_el_view.xml',
        'views/expert_view.xml',
        'views/feedback_view.xml',
    

   ],
    'application': True,
    'installable': True
}