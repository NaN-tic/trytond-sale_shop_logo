# This file is part of the sale_shop_logo module for Tryton.
# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
import unittest
import trytond.tests.test_tryton
from trytond.tests.test_tryton import ModuleTestCase


class SaleShopLogoTestCase(ModuleTestCase):
    'Test Sale Shop Logo module'
    module = 'sale_shop_logo'


def suite():
    suite = trytond.tests.test_tryton.suite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(
        SaleShopLogoTestCase))
    return suite