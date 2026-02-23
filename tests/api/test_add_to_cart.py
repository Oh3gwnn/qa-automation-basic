import os
import pytest
from src.clients.shopify_client import ShopifyClient
from src.contracts.schemas import AddToCartResponse

BASE_URL = os.getenv("BASE_URL")
VARIANT_ID = os.getenv("VARIANT_ID")
# VARIANT_ID = 12345678 # 테스트 실패용 더미 데이터

def test_add_to_cart_contract():
    """
    Contract:
    - 유효한 variant_id로 요청하면
    - 200 OK를 반환하고
    - 응답에 담긴 상품 정보가 포함되어야 한다
    """

    client = ShopifyClient(BASE_URL)
    # int() 형변환 주의(.env는 무조건 문자열로 읽음)
    res = client.add_to_cart(variant_id=int(VARIANT_ID), quantity=1)

    assert res.status_code == 200
    body = res.json()
    added = AddToCartResponse.model_validate(body["items"][0])
    print("ADD RESPONSE:", res.json()) # 테스트 확인용 로그
    
    assert added.id == int(VARIANT_ID)
    assert added.quantity == 1
    assert added.title

def test_cart_state_reflects_added_item():
    client = ShopifyClient(BASE_URL)

    # add
    res_add = client.add_to_cart(variant_id=int(VARIANT_ID), quantity=1)
    assert res_add.status_code == 200, res_add.text

    # verify cart
    res_cart = client.get_cart()
    assert res_cart.status_code == 200

    cart = res_cart.json()
    assert cart["item_count"] >= 1
    assert any(item["id"] == int(VARIANT_ID) for item in cart["items"])