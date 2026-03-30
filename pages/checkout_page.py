# pages/checkout_page.py
class CheckoutPage:
    def __init__(self, page):
        self.page = page
        self.first_name_input = page.locator("[data-test='firstName']")
        self.last_name_input = page.locator("[data-test='lastName']")
        self.zip_code_input = page.locator("[data-test='postalCode']")
        self.continue_button = page.locator("[data-test='continue']")
        self.finish_button = page.locator("[data-test='finish']")
        self.complete_header = page.locator(".complete-header")

        self.error_message = page.locator('[data-test="error"]')

    def fill_checkout_info(self, first, last, zip_code):
        self.first_name_input.fill(first)
        self.last_name_input.fill(last)
        self.zip_code_input.fill(zip_code)
        self.continue_button.click()

    def finish_checkout(self):
        self.finish_button.click()

    def get_error_message(self):
        return self.error_message.inner_text()