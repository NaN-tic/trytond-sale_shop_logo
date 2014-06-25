# This file is part of the sale_shop_logo module for Tryton.
# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
from trytond.pool import Pool
from .shop import *


def register():
    Pool.register(
        Shop,
        module='sale_shop_logo', type_='model')
