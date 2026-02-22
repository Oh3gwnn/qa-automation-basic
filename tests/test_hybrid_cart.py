import pytest
import os
from dotenv import load_dotenv
from src.clients.shopify_client import ShopifyClient
from playwright.sync_api import Page, expect

# .env 파일 로드
load_dotenv()

def test_api_add_to_cart_and_ui_verify(page: Page):
    # 설정 (실제 Shopify 스토어 URL과 테스트용 상품 ID 넣기)
    # BASE_URL = "https://sauce-demo.myshopify.com" 
    # VARIANT_ID = 611952521  # 테스트용 상품 번호

    BASE_URL = os.getenv("BASE_URL")
    VARIANT_ID = os.getenv("VARIANT_ID")

    # 1. API로 상품 담기
    client = ShopifyClient(BASE_URL)
    response = client.add_to_cart(variant_id=VARIANT_ID, quantity=2)
    assert response.status_code == 200

    # 2. API 세션의 쿠키를 Playwright 브라우저로 복사 (브릿지 역할)
    # requests의 쿠키를 playwright 형식으로 변환
    api_cookies = client.session.cookies.get_dict()
    playwright_cookies = [
        {"name": name, "value": value, "url": BASE_URL}
        for name, value in api_cookies.items()
    ]
    page.context.add_cookies(playwright_cookies)

    # 3. UI로 장바구니 페이지 접속
    page.goto(f"{BASE_URL}/cart")
    
    # 4. 검증: UI상에 상품이 있는지 확인

    # 예: 장바구니 아이템 개수가 '2'인지 확인
    # input 태그의 경우 text가 아니라 value를 확인해야 하므로 to_have_value

    # 모바일용 사이드바(drawer), 메인 장바구니(cart) 두 가지 중 .first 첫 번째 input 대상
    # quantity_input = page.locator('input[name="updates[]"]').first

    # 혹은 #cart 아이디를 가진 영역 안의 input만 지정
    quantity_input = page.locator('#cart input[name="updates[]"]')
    expect(quantity_input).to_have_value("2") 
    
    # 추가 검증: 상품 이름
    product_name = page.locator('.description h3 a').first 
    # 얘는 .first로 해서 passed했지만, 장기적으로는 #cart가 더 나은 방법
    expect(product_name).to_contain_text("Noir jacket")