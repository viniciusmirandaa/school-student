from odoo import fields, models, api
from datetime import datetime, date, timedelta
from odoo.exceptions import ValidationError
from odoo.exceptions import UserError
from odoo.tools.translate import _


class Hobbies(models.Model):
    _name = "hobby"

    name = fields.Char("Hobby")
