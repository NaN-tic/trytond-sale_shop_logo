# This file is part of the sale_shop_logo module for Tryton.
# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
from trytond.model import fields
from trytond.pool import PoolMeta

__all__ = ['Shop']


class Shop:
    __metaclass__ = PoolMeta
    __name__ = 'sale.shop'
    logo = fields.Binary('Logo')
