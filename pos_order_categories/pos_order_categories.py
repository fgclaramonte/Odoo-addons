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
from openerp import models, fields, api
from openerp import exceptions
from openerp.tools.translate import _


class order_categories (models.Model):
    _name = 'pos_order_categories.order_categories'
    category = fields.Many2one('product.category', string='Categoría',ondelete='restrict')
    quantity = fields.Integer(string='Cantidad')
    price = fields.Float(string='Precio total', digits=(16, 4))
    price_with_tax = fields.Float(string='Precio total con Impuestos', digits=(16, 4))
    session_id = fields.Many2one('pos.session',ondelete='restrict')


class pos_session (models.Model):
    _name = 'pos.session'
    _inherit = ['pos.session']

    order_categories_ids = fields.Many2many('pos_order_categories.order_categories','categorias','session_id', 'category_id', String="Categorías de productos", readonly=True)
    

    @api.multi
    def carga_categorias(self):
        self.ensure_one()
        line_obj = self.env['pos.order.line']
        product_obj = self.env['product.template']
        order_cat_obj = self.env['pos_order_categories.order_categories']
        
        # Limpio primero los registros para no acumular en distintas llamadas
        for session in self.env['pos.session'].search([('id','=',self.id)]):
            session_id = order_cat_obj.browse(session.id)
            session_id.unlink()

            order_cat_id = order_cat_obj.search([('session_id','=', session.id)])
            orderid = order_cat_obj.browse(order_cat_id.ids)
            cantidad = 0
            precio = 0
            precio_tax = 0
            for oid in orderid:
                res = oid.write({'quantity': cantidad, 'price': precio, 'price_with_tax': precio_tax})
        
        try:
            # Este bloque no es óptimo. Pero el número de iteraciones es mínimo.
            for session in self.env['pos.session'].search([('id','=',self.id)]):
                for orders in session.order_ids:
                    for order in orders:
                        for lines in order.lines:
                            for l in lines:
                                if order_cat_obj.search([('category','=', l.product_id.categ_id.id), ('session_id','=', session.id)]):
                                    order_cat_id = order_cat_obj.search([('category','=', l.product_id.categ_id.id), ('session_id','=', session.id)])
                                    orderid = order_cat_obj.browse(order_cat_id.id)
                                    cantidad = orderid.quantity + l.qty
                                    precio = orderid.price + l.price_subtotal
                                    precio_tax = orderid.price_with_tax + l.price_subtotal_incl
                                    res = orderid.write({'quantity': cantidad, 'price': precio, 'price_with_tax': precio_tax})
                                else:
                                    res = order_cat_obj.create({'category': l.product_id.categ_id.id, 'quantity': l.qty ,'price': l.price_subtotal, 'price_with_tax': l.price_subtotal_incl, 'session_id': session.id })
                                    session.order_categories_ids = [(4, res.id)]

        except exceptions.MissingError:
            raise exceptions.Warning("No ha sido posible")
            pass
        
        return True


order_categories()
pos_session()
