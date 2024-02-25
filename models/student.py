from odoo.models import Model
from odoo.fields import Char as String, Many2many

class Student(Model):
    _name = 'school.student'

    name: String = String(
        string='Name'
    )

    last_name: String = String(
        string='Last Name'
    )

    module_relation: Many2many = Many2many(
        comodel_name='school.module',
        relation='relation',
        column1='student_id',
        column2='module_id',
        string='Modules'
    )