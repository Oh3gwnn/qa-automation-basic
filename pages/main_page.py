from playwright.sync_api import Page, expect

# pages/main_page.py 초안~~~
class MainPage:
    def __init__(self, page: Page):
        self.page = page
        # Selectors
        self.page_title = page.locator(".title")
        self.add_to_cart_btn = page.locator("#add-to-cart-sauce-labs-backpack")
        self.cart_badge = page.locator(".shopping_cart_badge")

    # Assertions
    def verify_page_loaded(self):
        """로그인 후 상품 페이지로 잘 넘어왔는지 확인"""
        expect(self.page_title).to_have_text("Products")

    def add_first_item_to_cart(self):
        """첫 번째 상품(백팩)을 장바구니에 담기"""
        self.add_to_cart_btn.click()

    def verify_cart_count(self, expected_count: str):
        """장바구니 아이콘에 숫자가 제대로 뜨는지 확인 (상태 변화 검증)"""
        expect(self.cart_badge).to_have_text(expected_count)