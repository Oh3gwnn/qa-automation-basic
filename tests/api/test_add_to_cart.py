import os

from src.clients.shopify_client import ShopifyClient
from src.contracts.schemas import AddToCartResponse


BASE_URL = "https://sauce-demo.myshopify.com"
VARIANT_ID = 611945025   # 장바구니에 담은 상품


def test_add_to_cart_contract():
    """
    Contract:
    - 유효한 variant_id로 요청하면
    - 200 OK를 반환하고
    - 응답에 담긴 상품 정보가 포함되어야 한다
    """
    client = ShopifyClient(BASE_URL)

    res = client.add_to_cart(variant_id=VARIANT_ID, quantity=1)

    assert res.status_code == 200, res.text

    body = res.json()
    added = AddToCartResponse.model_validate(body)
    print("ADD RESPONSE:", res.json()) # 테스트 확인용 로그
    
    assert added.id == VARIANT_ID
    assert added.quantity == 1
    assert added.title

def test_cart_state_reflects_added_item():
    client = ShopifyClient(BASE_URL)

    # add
    res_add = client.add_to_cart(variant_id=VARIANT_ID, quantity=1)
    assert res_add.status_code == 200, res_add.text

    # verify cart
    res_cart = client.get_cart()
    assert res_cart.status_code == 200, res_cart.text

    cart = res_cart.json()
    assert cart["item_count"] >= 1
    assert any(item["id"] == VARIANT_ID and item["quantity"] >= 1 for item in cart["items"])