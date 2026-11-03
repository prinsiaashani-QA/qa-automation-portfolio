# QA Automation Portfolio

Playwright + Pytest (Python) automation tests for https://www.saucedemo.com (a public demo shop).

## Tech
Python, Playwright, Pytest, Git and GitHub

## What is covered
| Test | Type |
|---|---|
| Valid login (standard_user) | Positive |
| Locked out user | Negative |
| Wrong username and password | Negative |
| Empty username | Negative |
| Empty password | Negative |

## Concepts used
- Page Object Model (locators and actions of a page in one class)
- Data-driven tests with `pytest.mark.parametrize`
- Assertions with Playwright `expect` (auto-wait, no sleep)

## Project structure
    pages/login_page.py     LoginPage class (locators and actions)
    tests/test_login.py     1 positive test + 4 data-driven negative tests
    conftest.py             shared fixtures
    pytest.ini              pytest settings
    requirements.txt

## Setup
    pip install -r requirements.txt
    playwright install

## Run
    pytest -v
    pytest -v --headed

## Related project
[excel-test-runner](https://github.com/prinsiaashani-QA/excel-test-runner): write test cases in Excel, run them with Playwright, get Actual Result and Status back in Excel, with screenshot and video on failure.

## Planned
Fixtures for login, inventory and cart tests, smoke and regression markers, HTML report, GitHub Actions.
