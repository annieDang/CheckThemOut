import pytest
from src.pricing_rules import ThreeForTwoDeal, BulkDiscount, FreeBundle
from src.product import Product, Item

def test_three_for_two_deal(products):
    pricing_rule = ThreeForTwoDeal()
    product = products['atv']
    
    total_price = pricing_rule.apply(product, 3)
    assert total_price == 2 * product.price  # Buy 3, pay for 2

    total_price = pricing_rule.apply(product, 4)
    assert total_price == 3 * product.price  # Buy 4, pay for 3
    
    total_price = pricing_rule.apply(product, 6)
    assert total_price == 4 * product.price  # Buy 6, pay for 4

def test_bulk_discount(products):
    pricing_rule = BulkDiscount(4, 499.99)  # Bulk discount price for more than 4 items
    product = products['ipd']
    
    total_price = pricing_rule.apply(product, 4)
    assert total_price == 4 * product.price  # No discount for exactly 4 items

    total_price = pricing_rule.apply(product, 5)
    assert total_price == 5 * 499.99  # Discount for more than 4 items

    total_price = pricing_rule.apply(product, 10)
    assert total_price == 10 * 499.99  # Discount for 10 items

def test_free_bundle(products):
    pricing_rule = FreeBundle('vga')
    product = products['mbp']
    free_product = products['vga']
    
    total_price = pricing_rule.apply(product, 1)
    assert total_price == product.price  # Price remains the same, but free item logic should be handled elsewhere

    total_price = pricing_rule.apply(product, 3)
    assert total_price == 3 * product.price  # Price remains the same, but free item logic should be handled elsewhere

    # Additional logic should be tested in the checkout process to ensure free item is added correctly

if __name__ == "__main__":
    pytest.main()
