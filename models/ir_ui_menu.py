# -*- coding: utf-8 -*-
##############################################################################
#
#    custom_root_menu module for OpenERP, Allows to define a custom root menu per user
#    Copyright (C) 2016 SYLEAM Info Services (<http://www.Syleam.fr/>)
#              Sylvain Garancher <sylvain.garancher@syleam.fr>
#
#    This file is a part of custom_root_menu
#
#    custom_root_menu is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    custom_root_menu is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from openerp import models, api


class IrUiMenu(models.Model):
    _inherit = 'ir.ui.menu'

    @api.model
    @api.returns('ir.ui.menu')
    def get_user_roots(self):
        menu_domain = [('parent_id', '=', self.env.user.menu_id.id)]
        return self.search(menu_domain)

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: