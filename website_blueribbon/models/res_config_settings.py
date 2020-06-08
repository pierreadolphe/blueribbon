# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models
from odoo.tools.translate import html_translate

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    crm_model_form = fields.Html('Model Data',translate=html_translate)

    @api.model
    def get_values(self):
        res = super(ResConfigSettings, self).get_values()
        res['crm_model_form'] = self.env['ir.config_parameter'].sudo().get_param('website_blueribbon.crm_model_form')
        return res

    def set_values(self):
        self.env['ir.config_parameter'].sudo().set_param('website_blueribbon.crm_model_form', self.crm_model_form)
        super(ResConfigSettings, self).set_values()