{
    'name': 'NasirUddin',
    'version': '12.0.1.0.0',
    'category': 'Extra Tools',
    'summary': 'Odoo Development Tutorials For Beginners',
    'sequence': '-100',
    'license': 'AGPL-3',
    'author': 'Nasir Uddin',
    'maintainer': 'Nasir Uddin',
    'website': 'odoomates.com',
    'live_test_url': 'https://www.youtube.com/watch?v=BDepk0LhVuI&list=PLqRRLx0cl0hoJhjFWkFYowveq2Zn55dhM&index=1',
    'depends': ['sale'],
    'demo': ['mail'],
    'data': [
        'security/ir.model.access.csv',
        'wizard/cancel_appointment_view.xml',
         'views/menu.xml',
        'views/patients.xml',
        # 'views/female_patient_view.xml',
        'views/appointment_view.xml',
        'views/patient_tag.xml',
        'views/new_sale_order.xml'

    ],
    'images': ['static/description/icon.png'],
    'installable': True,
    'application': True,
    'auto_install': False,
}
# Video Explanation: https://www.youtube.com/watch?v=BDepk0LhVuI&list=PLqRRLx0cl0hoJhjFWkFYowveq2Zn55dhM&index=1
