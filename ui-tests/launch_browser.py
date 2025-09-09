from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    #launch the browser
    browser = playwright.chromium.launch(headless=False,slow_mo = 1000)
    #create new page
    page = browser.new_page()
    #visit the playwright websit
    page.goto("https://playwright.dev/python/docs/intro")
    #select the Docs button
    docs_button = page.get_by_role('link',name = "Docs")
    #clicking the docs button
    docs_button.click()
    #get the url of docs button
    print("Docs: ",page.url)

    browser.close()