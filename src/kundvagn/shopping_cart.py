from src.kundvagn.inventory import *


class ShoppingCartItem:
    def __init__(self, cart_item_id, name, price, amount_in_cart):
        self.id = cart_item_id
        self.name = name
        self.price = price
        self.amount_in_cart = amount_in_cart

# TODO testa denna
# kundvagnen har koppling till ett inventory från vilken artiklarna hämtas
class ShoppingCart:
    def __init__(self):
        self.inventory = Inventory()
        self.items_in_cart = {}

    def add_inventory_item(self, item: InventoryItem, amount):
        item = self.inventory.get_item(item.id)
        # om amount inte är större än noll, ge ValueError
        if amount <= 0:
            raise ValueError("amount must be higher than 0")
        try:
            self.inventory.reduce_amount_in_inventory(item, amount)
            # item_to_add_to_cart = self.inventory.get_item(item)
            self.items_in_cart[item] = ShoppingCartItem(item.id, item.name, item.price, amount )
        except ValueError as e:
            print(f"Fel: {e}")





        """
        if item not in self.inventory:
            raise ValueError(f"{item.name} not in inventory, cannot be put in shopping cart.")
        elif item in self.inventory:
            if self.inventory.get_item(item).amount < amount:
                raise ValueError(f"{item.name} can't put in {amount} items.")
            elif self.inventory.get_item(item).amount >= amount:
            """





