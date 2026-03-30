# tests/ui/test_checkout_flow.py
import pytest
import os
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.checkout_page import CheckoutPage


@pytest.mark.parametrize("first, last, zip_code, expected", [
    ("jane", "doe", "12345", "Thank you for your order!"), # 성공 케이스 - 정상 결제
    ("", "doe", "12345", "Error: First Name is required"), # 실패 케이스 - 이름 빠짐
    ("jane", "", "12345", "Error: Last Name is required"), # 실패 케이스 - 성 빠짐
    ("jane", "doe", "", "Error: Postal Code is required"), # 실패 케이스 - 우편번호 빠짐
])

# def test_full_checkout_path_success(page):
#     # 1. 로그인
#     login_page = LoginPage(page)
#     login_page.goto()
#     login_page.login(os.getenv("SAUCE_USERNAME"), os.getenv("SAUCE_PASSWORD"))

#     # 2. 상품 담기 및 장바구니 이동
#     main_page = MainPage(page)
#     main_page.add_first_item_to_cart()
#     page.click(".shopping_cart_link") # 장바구니 아이콘 클릭
#     page.click("[data-test='checkout']") # 체크아웃 버튼 클릭

#     # 3. 결제 정보 입력
#     checkout_page = CheckoutPage(page)
#     checkout_page.fill_checkout_info("jane", "doe", "12345")
    
#     # 4. 최종 결제 및 완료 확인
#     checkout_page.finish_checkout()
    
#     # "Thank you for your order!" 문구가 뜨는지 검증
#     assert page.locator(".complete-header").inner_text() == "Thank you for your order!"

def test_checkout_form_validation(page, first,last, zip_code, expected):
    # 1. 로그인
    login_page = LoginPage(page)
    login_page.goto()
    login_page.login(os.getenv("SAUCE_USERNAME"), os.getenv("SAUCE_PASSWORD"))

    # 2. 상품 담기 및 장바구니 이동
    main_page = MainPage(page)
    main_page.add_first_item_to_cart()
    page.click(".shopping_cart_link") # 장바구니 아이콘 클릭
    page.click("[data-test='checkout']") # 체크아웃 버튼 클릭

    # 3. 결제 정보 입력
    checkout_page = CheckoutPage(page)
    checkout_page.fill_checkout_info(first, last, zip_code)

    # 4. 검증 로직
    if "Thank you for your order!" in expected:
        checkout_page.finish_checkout()
        assert page.locator(".complete-header").inner_text() == expected
    else:
        assert checkout_page.get_error_message() == expected