import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://guu.ru/")
    page.locator("div:nth-child(2)").first.click()
    page.goto("https://guu.ru/")
    page.get_by_role("link", name="Подготовка к ЕГЭ, ОГЭ").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
