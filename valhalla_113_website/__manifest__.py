{
    'name': 'Valhalla 113 Website',
    'version': '18.0.1.0.1',
    'category': 'Website',
    'summary': 'Professional sports bar landing page for Valhalla 113 Grill & Bar.',
    'description': 'Adds a custom Valhalla 113 sports bar standalone website page with responsive design, sticky header, mobile menu, event cards, menu highlights, and contact section.',
    'author': 'Sheveion Callender',
    'website': 'https://www.spxcorp.net',
    'license': 'LGPL-3',
    'depends': ['website'],
    'data': [
        'views/valhalla_homepage.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            'valhalla_113_website/static/src/css/valhalla_113.css',
            'valhalla_113_website/static/src/js/valhalla_113.js',
        ],
    },
    'installable': True,
    'application': False,
}
