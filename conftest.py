import pytest
from pages.login_page import LoginPage


@pytest.fixture
def logged_in_page(page):
    lp = LoginPage(page)
    lp.open()
    lp.login("standard_user", "secret_sauce")
    return page