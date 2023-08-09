{
    'name': 'Crm Commission',
    'version': '16.0.1.0.0',
    'author': 'Ajit',
    'summary': 'Crm Commission introduction',
    'category': 'commission',
    'description’': 'Description of the Crm Commission',
    'sequence': 15,
    'depends': ['base_setup', 'crm', 'sale_management'],
    'data': [
        'security/ir.model.access.csv',
        'views/crm_commission_view.xml',
        'views/crm_team_view.xml',
        'views/crm_team_member_view.xml',
        'views/sale_order_inherit_view.xml',
        'views/res_users_view.xml'
    ],

    'installable': True,
    'application': True,
    'auto_install': False

}
