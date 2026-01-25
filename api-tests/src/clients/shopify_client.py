import requests


class ShopifyClient:
    def __init__(self, base_url: str):
        self.base_url = base_url.rstrip("/")
        self.session = requests.Session()

        # Shopify cart API에 필요한 최소 헤더
        self.session.headers.update({
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "X-Requested-With": "XMLHttpRequest",
            "Origin": self.base_url,
        })

    def add_to_cart(self, variant_id: int, quantity: int = 1):
        url = f"{self.base_url}/cart/add.js"
        data = {
            "id": variant_id,
            "quantity": quantity,
        }
        return self.session.post(url, data=data, timeout=10)