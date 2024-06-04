class Product:
    def __init__(self, product_id, name, price, pricing_rule=None):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.pricing_rule = pricing_rule
        
    def __str__(self):
        return f"Product(ID: {self.product_id}, Name: {self.name}, Price: {self.price}, Pricing Rule: {self.pricing_rule})"


class Item:
    def __init__(self, sku, product, status="in store"):
        self.sku = sku
        self.product = product
        self.status = status  # Initial status when the item is in store

    def update_status(self, new_status):
        self.status = new_status
        
    def __str__(self):
        return f"Item(SKU: {self.sku}, Product: {self.product.name}, Status: {self.status})"