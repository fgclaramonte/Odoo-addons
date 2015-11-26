from openerp.osv import osv, fields

class res_partner(osv.Model):
    _inherit = 'res.partner'
    _columns = {
        'ref_empresa': fields.char('Referencia de empresa', select=1),
    }


res_partner()
