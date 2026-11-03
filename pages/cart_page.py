class CartPage:
    def __init__(self, page):
        self.page = page
        self.items = page.locator(".cart_item")
        self.item_names = page.locator(".inventory_item_name")