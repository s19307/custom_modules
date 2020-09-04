# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from odoo.tools.float_utils import float_round


class HrEmployeePrivate(models.Model):
    """
    NB: Any field only available on the model hr.employee (i.e. not on the
    hr.employee.public model) should have `groups="hr.group_hr_user"` on its
    definition to avoid being prefetched when the user hasn't access to the
    hr.employee model. Indeed, the prefetch loads the data for all the fields
    that are available according to the group defined on them.
    """
    _inherit = ['hr.employee', ]

    reviews_count = fields.Integer(compute='_compute_reviews_count', string='Review Count')

    def _compute_reviews_count(self):
        # read_group as sudo, since review count is displayed on form view
        review_data = self.env['s19307_hr.employee.review'].sudo().read_group([('employee_id', 'in', self.ids)],
                                                                              ['employee_id'],
                                                                              ['employee_id'])
        result = dict((data['employee_id'][0], data['employee_id_count']) for data in review_data)
        for employee in self:
            employee.reviews_count = result.get(employee.id, 0)
