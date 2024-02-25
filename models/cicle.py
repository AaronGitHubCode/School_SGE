from odoo.models import Model
from odoo.fields import Char as String, One2many

class Cicle(Model):
    _name = 'school.cicle'

    name: String = String(
        string='Name'
    )

    module_relation: One2many = One2many(
        comodel_name='school.module',
        inverse_name='cicle_relation',
        string='Modules'
    )