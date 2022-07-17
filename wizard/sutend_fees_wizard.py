from odoo import fields, models, api
from datetime import datetime, date, timedelta
from odoo.exceptions import ValidationError
from odoo.exceptions import UserError
from odoo.tools.translate import _


class StudentFeesWizard(models.TransientModel):
    _name = 'student.fees.wizard'

    wizard_fees = fields.Integer(
        string="Total Fees",
    )

    def student_fees_button(self):
        self.env['school.student'].browse(self._context.get('active_ids')).update({'total_fees': self.wizard_fees})
        return True
