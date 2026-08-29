
class InventoryItem:
    def __init__(self, item_id, name, price, amount_in_stock):
        self.id = item_id
        self.name = name
        self.price = price
        self.amount_in_stock = amount_in_stock

""" Denna klass ska skapas enligt uppgiften. 
Håller koll på lagret: vilka produkter och antal. """

class Inventory:
    def __init__(self):
        self._items = {}


    # metoden ska ta emot ett InventoryItem
    def add_item_to_inventory(self, item:InventoryItem):
        self._items[item.id] = item


    # om det enbart står def get_item(self, item_id): så blir det varningar i PyCharm
    # därför gör jag tillägget att svaret kan vara antingen InventoryItem eller None
    def get_item(self, item_id) -> InventoryItem | None:
        return self._items.get(item_id)


    # Inventory är den klass som äger lagersaldot, den vet om det finns tillräckligt med artiklar eller inte.
    # ShoppingCart ska bara fråga och lita på svaret.
    # Inventory ska skydda lagret oavsett vem som anropar, och aldrig gå under 0
    def reduce_amount_in_inventory(self, item_id, amount):
        item = self.get_item(item_id)
        # om artikeln saknas i lagret så kastas ett ValueError
        if item is None:
            raise ValueError(f"Product with id {item_id} is not in inventory.")
        # artikel finns i lager
        # men för få artiklar på lager, kan inte lägga i kundvagnen
        if item.amount_in_stock < amount:
            raise ValueError(f"Only {item.amount_in_stock} items with id {item_id}, cannot reduce by {amount}.")
        # eller så finns det tillräckligt med artiklar på lagret
        item.amount_in_stock -= amount








