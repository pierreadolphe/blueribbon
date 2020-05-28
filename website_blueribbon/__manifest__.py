# -*- encoding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
  'name': 'Website Blueribbon',
  'category': "",
  'license': 'OPL-1',
  'version': '1.0',
  'summary': '',
  'description': '',
  'author': 'Synconics Technologies Pvt. Ltd.',
  'website': 'www.synconics.com',
  'depends': ['web_enterprise','website_crm','mass_mailing'],
  'data': [
      'data/website_data.xml',
      'data/website_crm_data.xml',
      'views/website_template.xml',
      'views/home_template.xml',
      'views/templates.xml',
      'views/case_study_template.xml',
      'views/privacy_policy.xml',
      'views/snippets.xml',
      'views/thank_you.xml',
      'views/res_config_settings.xml',
  ],
  'installable': True,
  'auto_install': False,
  'bootstrap': True,
  'application': True,
}