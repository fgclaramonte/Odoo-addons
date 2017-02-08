# -*- encoding: utf-8 -*-
##############################################################################
#    fp_custom
#    Copyright (c) 2016 Francisco Manuel García Claramonte <francisco@garciac.es>
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
    'name': 'Referencia de productos a Base de datos OpenBravo',
    'version': '8.0.0.1.0',
    'category': 'Product',
    'description': """
Modulo para referenciar productos externos
==========================================

Añade un campo para referencia de productos con base de datos OpenBravo
(Desarrollo a medida).

Publicado bajo licencia AGPL-v3.

Copyright (c) 2016 Francisco Manuel García Claramonte

    """,
    'author': 'Francisco M. García Claramonte',
    'website': 'http://www.garciac.es',
    'depends': [
        'product',
    ],
    'data': [
        'views/product_view.xml',
    ],
    "installable": True,
}
