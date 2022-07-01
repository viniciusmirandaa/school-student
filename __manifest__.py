{
    'name': 'School Student',
    'version': '15.0.0.0',
    'sequence': 2,
    'author': 'Vinicius Silva de Miranda',
    'license': 'LGPL-3',
    'summary': 'School Student Module',
    'depends': ['base', 'school'],
    'data': [
        'security/groups.xml',
        'security/ir.model.access.csv',
        'views/school_student_view.xml',
        'views/hobbies_view.xml',
    ],
    'installable': True,
    'application': True,
}
