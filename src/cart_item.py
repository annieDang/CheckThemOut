class CartItem:
    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity

    def get_total_price(self):
        return self.product.price * self.quantity

class BundleItem(CartItem):
    def __init__(self, items):
        self.items = items

    def get_total_price(self):
        return sum(item.get_total_price() for item in self.items)
