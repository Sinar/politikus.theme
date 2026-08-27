# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID

import unittest

from politikus.theme.testing import POLITIKUS_THEME_FUNCTIONAL_TESTING
from politikus.theme.testing import POLITIKUS_THEME_INTEGRATION_TESTING


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
        self.assertTrue(self.installer.is_product_installed(
            'politikus.theme'))

    def test_browserlayer(self):
        """Test that IPolitikusThemeLayer is registered."""
        from politikus.theme.interfaces import IPolitikusThemeLayer
        from plone.browserlayer import utils
        self.assertIn(
            IPolitikusThemeLayer,
            utils.registered_layers())

    def test_theme_registered(self):
        """Test that the politikus-theme is available, applied and enabled."""
        from plone.app.theming.interfaces import IThemeSettings
        from plone.app.theming.utils import getAvailableThemes
        from plone.registry.interfaces import IRegistry
        from zope.component import getUtility

        names = [info.__name__ for info in getAvailableThemes()]
        self.assertIn('politikus-theme', names)

        settings = getUtility(IRegistry).forInterface(IThemeSettings)
        self.assertTrue(settings.enabled)
        self.assertIn('politikus-theme', settings.currentTheme)


class TestThemeApplied(unittest.TestCase):
    """Functional test: the diazo theme wraps the rendered page."""

    layer = POLITIKUS_THEME_FUNCTIONAL_TESTING

    def test_theme_applied(self):
        """The rendered page is wrapped by the diazo theme."""
        from urllib.request import urlopen

        url = 'http://%s:%s/plone/' % (self.layer['host'], self.layer['port'])
        body = urlopen(url).read()
        self.assertIn(b'++theme++politikus-theme', body)


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
        self.installer.uninstall_product('politikus.theme')
        setRoles(self.portal, TEST_USER_ID, roles_before)

    def test_product_uninstalled(self):
        """Test if politikus.theme is uninstalled."""
        self.assertFalse(self.installer.is_product_installed(
            'politikus.theme'))
