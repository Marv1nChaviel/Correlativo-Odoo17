from odoo import models, fields, api

class CrmLead(models.Model):
    _inherit = 'crm.lead'

    correlativo = fields.Char(string='Correlativo', readonly=True, copy=False)

    @api.model
    def create(self, vals):
        if 'correlativo' not in vals:
            vals['correlativo'] = self.env['ir.sequence'].next_by_code('crm.lead.correlativo') or '/'
        return super(CrmLead, self).create(vals)
