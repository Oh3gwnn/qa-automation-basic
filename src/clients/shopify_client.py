import requests

class ShopifyClient:
    def __init__(self, base_url: str):
        self.base_url = base_url.rstrip("/")
        self.session = requests.Session()

        # Shopify cart API에 필요한 최소 헤더
        self.session.headers.update({
            "Accept": "application/json",
            "X-Requested-With": "XMLHttpRequest",
            "Origin": self.base_url,
        })

    def add_to_cart(self, variant_id: int, quantity: int = 1):
        url = f"{self.base_url}/cart/add.js"
        payload = {
            "items": [
                {
                    "id": int(variant_id),
                    "quantity": int(quantity)
                }
            ]
        }
        return self.session.post(url, json=payload, timeout=10)
    
    def get_cart(self):
        url = f"{self.base_url}/cart.js"
        return self.session.get(url, timeout=10)