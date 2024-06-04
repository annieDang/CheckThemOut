import pytest
from src.product import Product, Item

def test_product_initialization():
    product = Product('ipd', 'Super iPad', 549.99)
    assert product.product_id == 'ipd'
    assert product.name == 'Super iPad'
    assert product.price == 549.99
    assert product.pricing_rule is None

def test_product_with_pricing_rule():
    product = Product('ipd', 'Super iPad', 549.99, 'bulk_discount')
    assert product.product_id == 'ipd'
    assert product.name == 'Super iPad'
    assert product.price == 549.99
    assert product.pricing_rule == 'bulk_discount'

def test_item_initialization(products):
    product = products['ipd']
    item = Item('sku_ipd_1', product)
    assert item.sku == 'sku_ipd_1'
    assert item.product == product
    assert item.status == 'in store'

def test_item_update_status(products):
    product = products['ipd']
    item = Item('sku_ipd_1', product)
    item.update_status('scanned')
    assert item.status == 'scanned'
    item.update_status('payed')
    assert item.status == 'payed'

def test_product_str():
    product = Product('ipd', 'Super iPad', 549.99, 'bulk_discount')
    expected_str = 'Product(ID: ipd, Name: Super iPad, Price: 549.99, Pricing Rule: bulk_discount)'
    assert str(product) == expected_str

def test_item_str(products):
    product = products['ipd']
    item = Item('sku_ipd_1', product, 'in store')
    expected_str = 'Item(SKU: sku_ipd_1, Product: Super iPad, Status: in store)'
    assert str(item) == expected_str

if __name__ == "__main__":
    pytest.main()
