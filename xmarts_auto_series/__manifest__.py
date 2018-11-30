# -*- coding: utf-8 -*-
{
    'name': "Series Automaticas en Recepciones",

    'summary': """
        Genera Series/Lotes para las recepciones de proveedores de manera automatica.""",

    'description': """
        *Agrega boton para generar series en recepciones
        *Agrega campo de referencia interna en compañia
    """,

    'author': "Xmarts, Pablo Osorio",
    'website': "http://www.xmarts.com",

    'category': 'Uncategorized',
    'version': '0.1',

    'depends': ['base','stock','purchase'],

    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'reports/picking_operation.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}