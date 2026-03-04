import pytest
from pages.login_page import LoginPage
from pages.main_page import MainPage

def test_add_item_to_cart_success(page):
    # 1. 준비 및 실행: 로그인 (Arrange & Act)
    login_page = LoginPage(page)
    login_page.goto()
    login_page.login("standard_user", "secret_sauce")

    # 2. 상태 전이 확인: 메인 페이지 도착 (Assert)
    main_page = MainPage(page)
    main_page.verify_page_loaded()

    # 3. 실행: 장바구니 버튼 클릭 (Act)
    main_page.add_first_item_to_cart()

    # 4. 결과 검증: 장바구니 숫자 '1' 확인 (Assert)
    main_page.verify_cart_count("1")