
{
    'name': 'IT Equipment',
    'version': '1.0',
    'summary': 'Yêu Cầu Mua Thiết Bị IT',
    'author': 'Ngan Hoang',
    'category': 'Productivity',
    'depends': ['base', 'dtg_hr'],
    'data': [
        'security/ir.model.access.csv',
        'views/it_request_view.xml',
        'views/it_equipment_view.xml',
        'views/it_request_line_view.xml',
    ],
    'installable': True,
    'application': True,
}