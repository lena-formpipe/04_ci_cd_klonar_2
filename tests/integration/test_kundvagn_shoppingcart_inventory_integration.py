import pytest

from src.kundvagn.shopping_cart import *

"""
Gör ett integrationstest som kontrollerar:
 - att man inte kan lägga till saker i ShoppingCart som inte finns på lager i Inventory.
Till er hjälp får ni två klasser som beskriver produkterna, och funktionen som ska testas.
Item-klasserna har ingen logik, så de behöver inte testas.
"""

@pytest.fixture
def item_stol():
    return InventoryItem(item_id=1, name="stol", price=100, amount_in_stock=10)


@pytest.fixture
def inventory_empty():
    inv = Inventory()
    return inv

@pytest.fixture
def inventory_with_stol(inventory_empty, item_stol):
    inv = Inventory()
    inventory_empty.add_item_to_inventory(item_stol)
    return inv

@pytest.fixture
def cart_empty(inventory_empty):
    return ShoppingCart(inventory_empty)

@pytest.fixture
def cart_with_stol(inventory_with_stol):
    return ShoppingCart(inventory_with_stol)

def test_shopping_cart_add_inventory_item__item_not_exists_in_inventory(cart_empty):
    # arrange - cart skapas i fixture
    item_id_not_exist = 999
    amount_not_exist = 100
    # act
    with pytest.raises(ValueError):
        cart_empty.add_inventory_item(item_id_not_exist, amount_not_exist)

    assert cart_empty.items_in_cart == {}


# def test_shopping_cart_add_inventory_item__item_exists_in_inventory(item_stol, ):
def test_shopping_cart_add_inventory_item__item_exists_in_inventory(inventory_empty, item_stol ):
    # arrange - blev något fel efter ändring till fixture
    new_inventory = inventory_empty
    new_inventory.add_item_to_inventory(item_stol)
    cart = ShoppingCart(new_inventory)

    cart.add_inventory_item(item_stol.id, amount =2)

    assert cart.items_in_cart[1].amount_in_cart == 2
    assert new_inventory.get_item(1).amount_in_stock == 8


def test_shopping_cart_add_inventory_item__amount_too_few(cart_empty, inventory_empty, item_stol):
    # inv = Inventory()
    # cart = ShoppingCart(inv)
    inventory_empty.add_item_to_inventory(item_stol)
    # act
    with pytest.raises(ValueError):
        cart_empty.add_inventory_item(1, 20)

    assert cart_empty.items_in_cart == {}
    assert inventory_empty.get_item(1).amount_in_stock == 10

