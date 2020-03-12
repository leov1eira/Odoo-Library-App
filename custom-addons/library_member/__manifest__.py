{
    'name': 'Library Members and Borrowing',
    'description': 'Use library cards for people to borrow books.',
    'author': 'Ruivo',
    'depends': [
        'library_app',
    ],
    'data':[
        'views/book_view.xml',
        'security/library_security.xml',
        'security/ir.model.access.csv',
        'views/member_view.xml',
        'views/library_menu.xml',
    ],
    'application': False,
}

