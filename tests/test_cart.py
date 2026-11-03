import pytest
from playwright.sync_api import expect
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage


@pytest.mark.smoke
def test_inventory_shows_6_products(logged_in_page):
    inv = InventoryPage(logged_in_page)
    expect(inv.items).to_have_count(6)


@pytest.mark.smoke
def test_add_to_cart_updates_badge(logged_in_page):
    inv = InventoryPage(logged_in_page)
    inv.add_to_cart("sauce-labs-backpack")
    expect(inv.cart_badge).to_have_text("1")


@pytest.mark.regression
def test_cart_shows_added_item(logged_in_page):
    inv = InventoryPage(logged_in_page)
    inv.add_to_cart("sauce-labs-backpack")
    inv.open_cart()
    cart = CartPage(logged_in_page)
    expect(cart.items).to_have_count(1)
    expect(cart.item_names).to_have_text("Sauce Labs Backpack")


@pytest.mark.regression
def test_remove_from_cart(logged_in_page):
    inv = InventoryPage(logged_in_page)
    inv.add_to_cart("sauce-labs-backpack")
    inv.remove_from_cart("sauce-labs-backpack")
    expect(inv.cart_badge).to_have_count(0)