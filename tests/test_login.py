import pytest
from playwright.sync_api import expect
from pages.login_page import LoginPage

def test_valid_login(page):
    lp = LoginPage(page)
    lp.open()
    lp.login("standard_user", "secret_sauce")
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
    expect(page.locator(".title")).to_have_text("Products")


@pytest.mark.parametrize(
    "user, pwd, error_text",
    [
        ("locked_out_user", "secret_sauce", "locked out"),
        ("wrong_user", "wrong_pass", "do not match"),
        ("", "secret_sauce", "Username is required"),
        ("standard_user", "", "Password is required"),
    ],
    ids=["locked_user", "wrong_credentials", "empty_username", "empty_password"],
)
def test_invalid_login(page, user, pwd, error_text):
    lp = LoginPage(page)
    lp.open()
    lp.login(user, pwd)
    expect(page.locator("[data-test='error']")).to_contain_text(error_text)