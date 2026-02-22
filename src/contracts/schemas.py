from pydantic import BaseModel
from typing import Optional


class AddToCartResponse(BaseModel):
    id: int            # variant_id
    quantity: int
    title: str
    price: int         # cents
    sku: Optional[str] = None