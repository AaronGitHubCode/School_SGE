from odoo.models import Model
from odoo.fields import Char as String, Many2many, Many2one

class Module(Model):
    _name = 'school.module'

    name: String = String(
        string='Module'
    )

    cicle_relation: Many2one = Many2one(
        comodel_name='school.cicle',
        string='Cicles',
        ondelete='cascade'
    )

    student_relation: Many2many = Many2many(
        string='Students',
        comodel_name='school.student',
        relation='relation',
        column1='module_id',
        column2='student_id'
    )

    teacher_relation: Many2one = Many2one(
        string='Teachers',
        comodel_name='school.teacher'
    )
