# -*- coding: utf-8 -*-
from openerp.osv import fields, osv

class stock_picking(osv.osv):
    _inherit = "stock.picking"

    def do_print_picking(self, cr, uid, ids, context=None):
        '''This function prints the picking list'''
        context = dict(context or {}, active_ids=ids)
        return self.pool.get("report").get_action(cr, uid, ids, 'albaran_personalizado.report_picking', context=context)

stock_picking()
