class InventoryPage:
    def __init__(self, page):
        self.page = page
        self.items = page.locator(".inventory_item")
        self.cart_badge = page.locator(".shopping_cart_badge")
        self.cart_link = page.locator(".shopping_cart_link")

    def add_to_cart(self, product_id):
        self.page.locator(f"[data-test='add-to-cart-{product_id}']").click()

    def remove_from_cart(self, product_id):
        self.page.locator(f"[data-test='remove-{product_id}']").click()

    def open_cart(self):
        self.cart_link.click()