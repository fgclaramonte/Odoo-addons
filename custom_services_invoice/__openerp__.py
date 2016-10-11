# -*- encoding: utf-8 -*-
##############################################################################
#    custom_services_invoice
#    Copyright (c) 2015-2016 Francisco Manuel García Claramonte <francisco@garciac.es>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published
#    by the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
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
    'name': 'Personalización genérico de informe de Factura para servicios',
    'version': '8.0.0.1.0',
    'author': 'Francisco M. García Claramonte',
    'category': 'garciac.es',
    'description': """
Módulo para personalizar el informe de factura de servicios
===========================================================

    Este módulo personalizar el informe de factura para imprimir.
    El formato se ajusta a una facturación de servicios en la que
    no es necesario desglosar los impuestos para cada linea. 
    Solo es necesario especificarlos en el total
    
    Publicado bajo licencia AGPL-v3
   
    Copyright (c) 2015-2016 Francisco Manuel García Claramonte
""",
    'website':'http://garciac.es',
    'depends': [
        'account',
    ],
    'data': [
        'views/report_invoice.xml',
        'views/external_layout_header.xml',
        'views/external_layout_footer.xml',
    ],
    "installable": True,
}
