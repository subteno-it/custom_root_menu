# -*- coding: utf-8 -*-
# Copyright 2016 SYLEAM Info Services
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, api


class IrUiMenu(models.Model):
    _inherit = 'ir.ui.menu'

    @api.model
    @api.returns('ir.ui.menu')
    def get_user_roots(self):
        menu_domain = [('parent_id', '=', self.env.user.menu_id.id)]
        return self.search(menu_domain)

