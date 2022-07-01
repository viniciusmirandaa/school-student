from odoo import fields, models, api
from datetime import datetime, date, timedelta
from odoo.exceptions import ValidationError
from odoo.exceptions import UserError
from odoo.tools.translate import _


class SchoolStudent(models.Model):
    _name = 'school.student'
    _description = 'school_student.school_student'

    name = fields.Char(
        string="Student Name",
    )
    school_id = fields.Many2one(
        comodel_name="school",
        string="School Name",
        required=True,
    )
    hobby_list = fields.Many2many(
        "hobby",
        "school_hobby_rel",
        "student_id",
        "hobby_id",
        string="Hobby List",
    )
    # is_virtual_school = fields.Boolean(
    #     related="school_id.is_virtual_class",
    #     string="Is Virtual Class",
    #     store=True
    # )
    # school_address = fields.Text(
    #     related="school_id.address",
    #     string="Address",
    #     help="This is school address."
    # )
    currency_id = fields.Many2one(
        "res.currency",
        string="Currency"
    )
    student_fees = fields.Monetary(
        string="Student Fees",
        index=True
    )
    total_fees = fields.Float(
        string="Total Fees",
        default=200
    )
    ref_id = fields.Reference(
        [
            ('school', 'School'),
            ('account.move', 'Invoice')
        ],
        string="Reference Field"
    )


class School(models.Model):
    _inherit = "school"

    student_list = fields.One2many(
        comodel_name="school.student",
        inverse_name="school_id"
    )
