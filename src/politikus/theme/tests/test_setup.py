# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from politikus.theme.testing import POLITIKUS_THEME_INTEGRATION_TESTING  # noqa: E501
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID

import unittest


try:
    from Products.CMFPlone.utils import get_installer
except ImportError:
    get_installer = None


class TestSetup(unittest.TestCase):
    """Test that politikus.theme is properly installed."""

    layer = POLITIKUS_THEME_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        if get_installer:
            self.installer = get_installer(self.portal, self.layer['request'])
        else:
            self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if politikus.theme is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'politikus.theme'))

    def test_browserlayer(self):
        """Test that IPolitikusThemeLayer is registered."""
        from politikus.theme.interfaces import (
            IPolitikusThemeLayer)
        from plone.browserlayer import utils
        self.assertIn(
            IPolitikusThemeLayer,
            utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = POLITIKUS_THEME_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        if get_installer:
            self.installer = get_installer(self.portal, self.layer['request'])
        else:
            self.installer = api.portal.get_tool('portal_quickinstaller')
        roles_before = api.user.get_roles(TEST_USER_ID)
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.installer.uninstallProducts(['politikus.theme'])
        setRoles(self.portal, TEST_USER_ID, roles_before)

    def test_product_uninstalled(self):
        """Test if politikus.theme is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'politikus.theme'))

    def test_browserlayer_removed(self):
        """Test that IPolitikusThemeLayer is removed."""
        from politikus.theme.interfaces import \
            IPolitikusThemeLayer
        from plone.browserlayer import utils
        self.assertNotIn(
            IPolitikusThemeLayer,
            utils.registered_layers())
