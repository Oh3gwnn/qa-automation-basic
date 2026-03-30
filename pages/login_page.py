# pages/login_page.py
import os

from playwright.sync_api import Page, expect

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.username_input = page.locator('#user-name')
        self.password_input = page.locator('#password')
        self.login_button = page.locator('#login-button')
        self.error_message = page.locator('[data-test="error"]')
        self.page_title = page.locator('.title')

    def goto(self, target="UI", path=""):
        if target == "UI":
            url = os.getenv("UI_BASE_URL")
        elif target == "API":
            url = os.getenv("API_BASE_URL")
        else:
            url = target
            
        # 주소 뒤에 경로를 붙여서 이동 (url이 None이 아닐 때)
        full_url = f"{url.rstrip('/')}/{path.lstrip('/')}" if url else url
        self.page.goto(full_url)

    def login(self, username, password):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()

    def expect_login_success(self):
        # lambda -> re
        # expect(self.page).to_have_url(lambda url: "/inventory" in url)
        # expect(self.page_title).to_have_text('Products')
        
        import re
        expect(self.page).to_have_url(re.compile(r".*/inventory\.html"))
        expect(self.page_title).to_have_text('Products')

    def expect_login_failure(self):
        expect(self.error_message).to_be_visible()