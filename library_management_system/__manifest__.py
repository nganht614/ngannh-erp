
{
    'name': 'Library Management',
    'version': '1.0',
    'summary': 'Hệ thống Quản lý Thư viện',
    'author': 'Ngan Hoang',
    'category': 'Productivity',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/library_book_view.xml',
        'views/library_author_view.xml',
        'views/library_category_view.xml',
        'views/library_loan_view.xml',
        'views/library_readers_view.xml',
    ],
    'installable': True,
    'application': True,
}