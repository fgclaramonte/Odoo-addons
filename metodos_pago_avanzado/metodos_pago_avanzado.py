# -*- coding: utf-8 -*-

from openerp.osv import fields, osv
from openerp import api

class metodos_pago(osv.Model):
    _name = 'metodos.pago'
    _description = 'Modos de pago para Contactos'
    _columns = {
        'name': fields.char('Método de pago'),
    }

   
class res_partner(osv.Model):
    _inherit = 'res.partner'
    _columns = {
        'metodos_pago': fields.many2one('metodos.pago', 'Método de pago', ondelete='set null'),
        }

class account_invoice(osv.Model):
    _inherit = 'account.invoice'
    _columns = {
        'metodos_pago': fields.many2one('metodos.pago', 'Método de pago', ondelete='set null'),
    }

    @api.multi
    def onchange_partner_id(self, type, partner_id, date_invoice=False,
                            payment_term=False, partner_bank_id=False, company_id=False):
        metodos_pago = False
        if partner_id:
            p = self.env['res.partner'].browse(partner_id)
            metodos_pago = p.metodos_pago

        self = self.with_context(metodos_pago=metodos_pago)
        result = super(account_invoice, self).onchange_partner_id(type, partner_id, date_invoice, payment_term, partner_bank_id, company_id)
        result['value'].update({'metodos_pago': metodos_pago})
        return result
            
    
res_partner()
account_invoice()
