# QA Automation Portfolio

Playwright + Pytest (Python) tests for https://www.saucedemo.com

## What is inside
- Page Object Model (pages/login_page.py)
- Valid login test
- Data-driven negative tests using parametrize

## Setup
    pip install -r requirements.txt
    playwright install

## Run
    pytest -v
    pytest -v --headed
