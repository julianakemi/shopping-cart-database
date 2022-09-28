from pydantic import BaseModel, Field
from typing import List
from functools import reduce

from src.schemas.order import UserSchema
from src.schemas.cart_item import CartItemSchema

class Cart(BaseModel):
    user: UserSchema
    product_list: List[CartItemSchema] = []
    total_price = Decimal = Field(max_digits=10, decimal_places=2)
    number_of_itens: int