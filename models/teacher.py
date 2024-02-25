from odoo.models import Model
from odoo.fields import Char as String, One2many
class Teacher(Model):
    _name = 'school.teacher'

    name: String = String(
        string='Name'
    )

    last_name: String = String(
        string='Last Name'
    )

    module_relation: One2many = One2many(
        comodel_name='school.module',
        inverse_name='teacher_relation',    
        string='Modules'
    )