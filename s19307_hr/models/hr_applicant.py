from odoo import api, fields, models, _


class Applicant(models.Model):
    _inherit = ["hr.applicant", ]

    cv_file = fields.Binary(string='CV File', attachment=True)
    cv_file_name = fields.Char("CV File Name")
    partner_linkedin = fields.Char('LinkedIn profile')
