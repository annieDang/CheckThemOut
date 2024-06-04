from src.pricing_rules import FreeBundle
from src.product import Item
from collections import defaultdict

class Checkout:
    def __init__(self, inventory):
        self.inventory = inventory
        self.scanned_items = []
        self.item_counts = {}

    def scan(self, sku):
        item = self.inventory.reduce_stock(sku)
        item.update_status("scanned")
        self.scanned_items.append(item)

        # Update item counts
        product_id = item.product.product_id
        if product_id in self.item_counts:
            self.item_counts[product_id] += 1
        else:
            self.item_counts[product_id] = 1

    def calculate_free_items(self):
        free_items = defaultdict(int)
        for item in self.scanned_items:
            product = item.product
            count = self.item_counts[product.product_id]
            if isinstance(product.pricing_rule, FreeBundle):
                print(27,product.pricing_rule.free_product_sku)
                free_items[product.pricing_rule.free_product_sku] += count
        return free_items

    def reduce_free_items(self, free_items):
         for free_product_id, count in free_items.items():
            free_items_list = [
                item for item in self.scanned_items
                if item.product.product_id == free_product_id and item.status != "payed"
            ]
            for i in range(min(count, len(free_items_list))):
                free_items_list[i].update_status("payed")
                self.item_counts[free_product_id] -= 1
                if self.item_counts[free_product_id] == 0:
                    del self.item_counts[free_product_id]

    def total(self):
        free_items = self.calculate_free_items()
        self.reduce_free_items(free_items)

        total = 0
        for product_id, count in self.item_counts.items():
            product = self.inventory.find_product(product_id)
            if product.pricing_rule:
                total += product.pricing_rule.apply(product, count)
            else:
                total += product.price * count

        # Update status to "payed" for all scanned items
        for item in self.scanned_items:
            item.update_status("payed")

        self.scanned_items.clear()  # Clear the scanned items after processing
        self.item_counts.clear()    # Clear the item counts after processing

        return total
