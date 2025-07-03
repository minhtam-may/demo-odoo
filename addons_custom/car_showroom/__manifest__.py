{
    'name': 'Car Showroom Management',
    'version': '1.0',
    'summary': 'Module quản lý showroom ô tô',
    'description': """
        Module này quản lý danh mục xe, hình ảnh, và tồn kho của showroom ô tô.
        Các tính năng bao gồm:
        - Quản lý danh sách xe (CRUD)
        - Quản lý hình ảnh xe
        - Theo dõi tồn kho
    """,
    'author': 'Your Name',
    'category': 'Business',
    'license': 'LGPL-3',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/car_views.xml',
    ],
    'installable': True,
    'application': True,
}