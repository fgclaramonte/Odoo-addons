# -*- coding: utf-8 -*-
#from openerp import models, fields, api
from openerp.osv import fields, osv

class product_bodega_origen(osv.Model):
    _name = 'product.bodega.origen'
    _description = 'Datos de origen para productos de bodega'
    _columns = {
        'name': fields.char('Origen'),
        #'origen_id': fields.one2many('product.template','origen', 'Origen'),
    }

class product_bodega_bodega(osv.Model):
    _name = 'product.bodega.bodega'
    _description = 'Datos de bodega para productos de bodega'
    _columns = {
        'name': fields.char('Bodega'),
        #'bodega_id': fields.one2many('product.template','bodega', 'Bodega'),
    }

    
class product_template(osv.Model):
    _inherit = 'product.template'
    _columns = {
        'origen': fields.many2one('product.bodega.origen', 'Origen', ondelete='set null'),
        'bodega': fields.many2one('product.bodega.bodega', 'Bodega', ondelete='set null'),
        }

product_template()

