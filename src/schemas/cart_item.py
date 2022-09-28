from pydantic import BaseModel
from src.schemas.product import ProductSchema

class CartItemSchema(BaseModel):
    product: ProductSchema
    quantity: int