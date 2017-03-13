# -*- encoding: utf-8 -*-
##############################################################################
#    pos_order_categories
#    Copyright (c) 2017 Francisco Manuel García Claramonte <francisco@garciac.es>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    'name': 'Pedidos de TPV clasificados por categorías de producto',
    'version': '8.0.0.1.5',
    'category': 'Tools',
    'description': """
Consulta de pedidos por sesión de TPV
=====================================

Este módulo añade al modelo de Sesión de TPV la conuslta de todos los pedidos,
agrupados por las categorías de los productos vendidos durante toda la sesión.
 

Publicado bajo licencia AGPL-v3.

Copyright (c) 2017 Francisco Manuel García Claramonte


    """,
    'author': 'Francisco M. García Claramonte',
    'website': 'http://www.garciac.ess',
    'depends': [
        'point_of_sale',
        'product',
    ],
    'data': [
        'views/point_of_sale_view.xml',
        'security/ir.model.access.csv',
    ],
    "installable": True,
}
