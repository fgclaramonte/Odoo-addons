# -*- coding: utf-8 -*-
{
   'name': 'Métodos de pago por cliente.',
   'version': '0.22',
   'author': 'Francisco M. Garcia (garciac.es)',
   'category': 'Garciac.es',
   'depends': ['base','account'],
    'website': 'https://www.garciac.es',
    'description': """
Métodos de pago avanzado. Asociado a cliente y factura
=======================================================

Este módulo añade el campo de método de pago relacionado con los contactos y 
las facturas.

El objetivo es asociar un método de pago por cliente, e incluirlo en los informes de facturas.

Publicado bajo licencia GPL-v3
    """,
   'data': [
       'metodos_pago_avanzado_view.xml',
       'metodos_pago_avanzado_data.xml',
       'security/ir.model.access.csv',
        ]

}
