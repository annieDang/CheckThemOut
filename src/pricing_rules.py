from abc import ABC, abstractmethod

class PricingRule(ABC):
    @abstractmethod
    def apply(self, product, quantity):
        pass

class ThreeForTwoDeal(PricingRule):
    def apply(self, product, quantity):
        discount_quantity = quantity - (quantity // 3)
        return discount_quantity * product.price

class BulkDiscount(PricingRule):
    def __init__(self, min_quantity, discounted_price):
        self.min_quantity = min_quantity
        self.discounted_price = discounted_price

    def apply(self, product, quantity):
        if quantity > self.min_quantity:
            return quantity * self.discounted_price
        return quantity * product.price

class FreeBundle(PricingRule):
    def __init__(self, free_product_sku):
        self.free_product_sku = free_product_sku

    def apply(self, product, quantity):
        return quantity * product.price  # Pricing remains the same, but will add free products elsewhere
