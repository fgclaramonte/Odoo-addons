# -*- coding: utf-8 -*-
{
   'name': 'Modelo de datos para catálogo de vinos',
   'version': '1.4',
   'author': 'Francisco M. Garcia (garciac.es)',
   'category': 'Garciac.es',
   'depends': ['product'],
    'website': 'https://www.garciac.es',
    'description': """
Módulo para modelo de datos de bodega de vinos
==============================================

Este módulo añade campos específicos para gestión de bodegas de vinos.
    Como son: Origen (Denominación de origen) del producto y Bodega del producción.

El módulo permite agrupar registros en vistas listado y kanvan con ambos campos.

Publicado bajo licencia GPL-v3
    """,
   'data': [
       'modelo_datos_bodega_view.xml',
       'modelo_datos_bodega_data.xml',
       'security/ir.model.access.csv',
        ]

}
