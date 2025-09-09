from playwright.sync_api import sync_playwright

with sync_playwright() as p:

    browser_launch = p.chromium.launch(headless = False,slow_mo = 3000)
    page = browser_launch.new_page()
    page.goto("https://www.saucedemo.com/")
    user_name = page.get_by_placeholder("Username").fill("standard_user")
    pass_word = page.get_by_placeholder("Password").fill("secret_sauce")
    login_button = page.get_by_role("button",name="Login").click()
    item_selection = page.get_by_text("Sauce Labs Backpack").click()
    add_to_cart = page.get_by_role("button",name="Add to cart").click()
    shopping_cart = page.locator('[data-test="shopping-cart-link"]').click()
