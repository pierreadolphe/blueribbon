# -*- coding: utf-8 -*-
# Part of Odoo. See COPYRIGHT & LICENSE files for full copyright and licensing details.

from odoo import http, tools, _
from odoo.http import request

class Websiteblueribbon(http.Controller):

    @http.route(['/case-study'], type='http', auth="public", website=True)
    def case_study(self, **kw):
        return request.render("website_blueribbon.case_study")

    @http.route(['/terms-and-conditions'], type='http', auth="public", website=True)
    def privacy_policy(self, **kw):
        return request.render("website_blueribbon.privacy_policy")


    @http.route(['/thank-you'], type='http', auth="public", website=True)
    def rb_thank_you(self, **kw):
        return request.render("website_blueribbon.rb_thank_you")