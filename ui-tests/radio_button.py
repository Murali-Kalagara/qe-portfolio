from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=3000)
    page = browser.new_page()
    page.goto("https://bootswatch.com/default/")
    
    radio_button = page.get_by_role(
        "radio",
        name="Option two can be something else and selecting it will deselect option one"
    )
    radio_button.click()
    
    browser.close()
