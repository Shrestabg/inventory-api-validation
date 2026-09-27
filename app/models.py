from pydantic import BaseModel


class Product(BaseModel):
    id: int
    name: str
    price: float
    stock: int


class ProductCreate(BaseModel):
    name: str
    price: float
    stock: int