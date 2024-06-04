import pytest
from src.inventory import Inventory
from src.product import Item

@pytest.fixture
def inventory():
    return Inventory()

@pytest.fixture
def item(products):
    return Item('sku_ipd_1', products['ipd'])

def test_initial_stock(inventory):
    assert inventory.get_stock('ipd') == 0

def test_add_stock(inventory, item):
    inventory.add_stock(item)
    assert inventory.get_stock('ipd') == 1

def test_reduce_stock(inventory, item):
    inventory.add_stock(item)
    inventory.reduce_stock('sku_ipd_1')
    assert inventory.get_stock('ipd') == 0

def test_reduce_stock_insufficient(inventory):
    with pytest.raises(ValueError):
        inventory.reduce_stock('sku_ipd_1')

def test_find_item(inventory, item):
    inventory.add_stock(item)
    found_item = inventory.find_item('sku_ipd_1')
    assert found_item == item

def test_find_item_not_found(inventory):
    found_item = inventory.find_item('sku_ipd_1')
    assert found_item is None
