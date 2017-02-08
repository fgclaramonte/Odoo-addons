# -*- encoding: utf-8 -*-
##############################################################################
#    product_supplier_price_wizard
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


class ProductPriceWizard(models.TransientModel):
    _name = 'product.template.precios_proveedor_wizard'

    @api.multi
    def actualiza_todos_precios(self):
        self.ensure_one()
        
        prod_obj = self.env['product.template']
        ## Actualiza todos los productos
        all_regs = prod_obj.search([])

        pricelist_obj = self.env['pricelist.partnerinfo']
        
        for reg in all_regs:
            if reg.precio_proveedor:
                for seller in reg.seller_ids:
                    proveedor = seller.name
                    lista_precios = seller.pricelist_ids
                    if not lista_precios:
                        pricelist = pricelist_obj.create({'suppinfo_id': seller.id, 'price' : reg.precio_proveedor, 'min_quantity': 1})
                
                    for l in lista_precios:
                        # En este punto se puede elegir la lista que se actualiza. Por proveedor.
                        cant = l.min_quantity
                        pricelist = pricelist_obj.browse(l.id)
                        res = pricelist.write({'price' : reg.precio_proveedor, 'min_quantity': 1})

    @api.multi
    def actualiza_precios(self):
        self.ensure_one()
        
        prod_obj = self.env['product.template']
        active_ids = self.env.context['active_ids'] or []
        all_regs = prod_obj.browse(active_ids)

        pricelist_obj = self.env['pricelist.partnerinfo']
        
        for reg in all_regs:
            if reg.precio_proveedor:
                for seller in reg.seller_ids:
                    proveedor = seller.name
                    lista_precios = seller.pricelist_ids
                    if not lista_precios:
                        pricelist = pricelist_obj.create({'suppinfo_id': seller.id, 'price' : reg.precio_proveedor, 'min_quantity': 1})
                
                    for l in lista_precios:
                        # En este punto se puede elegir la lista que se actualiza. Por proveedor.
                        cant = l.min_quantity
                        pricelist = pricelist_obj.browse(l.id)
                        res = pricelist.write({'price' : reg.precio_proveedor, 'min_quantity': 1})
