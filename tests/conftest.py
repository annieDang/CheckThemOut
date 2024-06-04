import pytest
from src.product import Product, Item
from src.pricing_rules import ThreeForTwoDeal, BulkDiscount, FreeBundle

@pytest.fixture
def products():
    return {
        'ipd': Product('ipd', 'Super iPad', 549.99, BulkDiscount(4, 499.99)),
        'mbp': Product('mbp', 'MacBook Pro', 1399.99, FreeBundle('vga')),
        'atv': Product('atv', 'Apple TV', 109.50, ThreeForTwoDeal()),
        'vga': Product('vga', 'VGA adapter', 30.00),
    }

@pytest.fixture
def items(products):
    items = []
    for i in range(10):
        items.append(Item(f'sku_ipd_{i}', products['ipd']))
        items.append(Item(f'sku_mbp_{i}', products['mbp']))
        items.append(Item(f'sku_atv_{i}', products['atv']))
        items.append(Item(f'sku_vga_{i}', products['vga']))
    return items
