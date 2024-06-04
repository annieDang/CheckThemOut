import pytest
from src.checkout import Checkout
from src.inventory import Inventory
from src.product import Item

@pytest.fixture
def inventory(items):
    inv = Inventory()
    for item in items:
        inv.add_stock(item)
    return inv

@pytest.fixture
def checkout(inventory):
    return Checkout(inventory)

def test_scenario_1(checkout):
    """
    Test scenario where 3 Apple TVs and 1 VGA adapter are scanned.
    Expected total: $249.00
    """
    checkout.scan('sku_atv_1')
    checkout.scan('sku_atv_2')
    checkout.scan('sku_atv_3')
    checkout.scan('sku_vga_1')
    assert checkout.total() == 249.00

def test_scenario_2(checkout):
    """
    Test scenario where multiple items are scanned:
    2 Apple TVs, 5 Super iPads.
    Expected total: $2718.95
    """
    checkout.scan('sku_atv_1')
    checkout.scan('sku_ipd_1')
    checkout.scan('sku_ipd_2')
    checkout.scan('sku_atv_2')
    checkout.scan('sku_ipd_3')
    checkout.scan('sku_ipd_4')
    checkout.scan('sku_ipd_5')
    assert checkout.total() == 2718.95

def test_scenario_3(checkout):
    """
    Test scenario where a MacBook Pro, VGA adapter, and a Super iPad are scanned.
    Expected total: $1949.98
    """
    checkout.scan('sku_mbp_1')
    checkout.scan('sku_vga_1')
    checkout.scan('sku_ipd_1')
    assert checkout.total() == 1949.98

def test_insufficient_stock(checkout):
    """
    Test scenario where more items are scanned than are in stock.
    Expected behavior: Raise ValueError
    """
    with pytest.raises(ValueError):
        for _ in range(11):
            checkout.scan('sku_ipd_1')

def test_item_status_after_scan(checkout):
    """
    Test the status of an item after it has been scanned.
    Expected status: 'scanned'
    """
    checkout.scan('sku_ipd_1')
    scanned_item = next(item for item in checkout.scanned_items if item.sku == 'sku_ipd_1')
    assert scanned_item.status == 'scanned'

def test_item_status_after_total(checkout):
    """
    Test the status of an item after the total has been calculated.
    Expected status: 'payed'
    """
    checkout.scan('sku_ipd_1')
    scanned_item = next(item for item in checkout.scanned_items if item.sku == 'sku_ipd_1')
    assert scanned_item.status == 'scanned'
    checkout.total()
    assert len(checkout.scanned_items) == 0
