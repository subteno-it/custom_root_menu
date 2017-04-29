# -*- coding: utf-8 -*-
# Copyright 2016 SYLEAM Info Services
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo.tests import common


class TestProductProduct(common.TransactionCase):
    def setUp(self):
        super(TestProductProduct, self).setUp()

        self.user = self.env.user

    def test_00_no_custom_menu(self):
        """
        Check that all menus without parent are taken when the user has no custom root menu
        """
        self.user.menu_id = False
        root_menus = self.env['ir.ui.menu'].sudo(self.user).get_user_roots()
        all_root_menus = self.env['ir.ui.menu'].search([('parent_id', '=', False)])
        self.assertEqual(root_menus, all_root_menus)

    def test_01_with_custom_menu(self):
        """
        Check that all menus without parent are taken when the user has no custom root menu
        """
        self.user.menu_id = self.env['ir.ui.menu'].search([('child_id', '!=', False)], limit=1)
        root_menus = self.env['ir.ui.menu'].sudo(self.user).get_user_roots()
        all_root_menus = self.user.menu_id.child_id
        self.assertEqual(root_menus, all_root_menus)

