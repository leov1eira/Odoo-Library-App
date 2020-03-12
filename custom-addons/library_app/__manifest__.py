{
    'name': 'Library Management Application',
    'description': 'Library books, members and book borrowing.',
    'author': 'Leonardo',
    'depends': ['base'],
    'application': True,
    'data': [
        'security/library_security.xml',
        'views/library_menu.xml',
        'security/ir.model.access.csv',
        'views/book_view.xml',
        'views/book_list_template.xml'
    ],
    'demo':[
        'data/book_demo.xml',
    ]
}
