class Inventory:
    def __init__(self):
        self.stock = {}

    def add_stock(self, item):
        if self.find_item(item.sku):
            raise ValueError(f"Item with SKU {item.sku} already exists in the inventory.")
        if item.product.product_id not in self.stock:
            self.stock[item.product.product_id] = []
        self.stock[item.product.product_id].append(item)

    def reduce_stock(self, sku):
        item = self.find_item(sku)
        if item:
            self.stock[item.product.product_id].remove(item)
            return item
        else:
            raise ValueError(f"Not enough stock for item with SKU {sku}.")

    def get_stock(self, product_id):
        return len(self.stock.get(product_id, []))

    def find_item(self, sku):
        for items in self.stock.values():
            for item in items:
                if item.sku == sku:
                    return item
        return None
        
    def find_product(self, product_id):
        if product_id in self.stock:
            items = self.stock[product_id]
            if items:
                return items[0].product
        return None