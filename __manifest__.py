{
    'name': 'CRM Correlativo',
    'version': '1.0',
    'category': 'CRM',
    'summary': 'Genera un correlativo al crear una oportunidad en el CRM',
    'depends': ['crm'],
    'data': [
        'data/ir_sequence_data.xml',
        'views/crm_lead_views.xml',
    ],
    'installable': True,
    'application': False,
}
