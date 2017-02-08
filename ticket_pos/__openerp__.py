# -*- coding: utf-8 -*-
{
   'name': 'Tickets POS personalizados.',
   'version': '8.0.1.4',
   'author': 'Francisco M. Garcia (garciac.es)',
   'category': 'Point of Sale',
   'depends': ['point_of_sale','sale_stock','decimal_precision'],
   'data': [
       'views/point_of_sale.xml',
   ],
   'qweb' : [
       'static/src/xml/pos.xml',
   ]
}
