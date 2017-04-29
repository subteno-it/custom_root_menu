# -*- coding: utf-8 -*-
# Copyright 2017 SYLEAM Info Services
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields


class ResUsers(models.Model):
    _inherit = 'res.users'

    menu_id = fields.Many2one('ir.ui.menu', string='Default menu', help='Set custom menu.')

