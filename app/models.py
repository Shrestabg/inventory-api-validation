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


class ReserveRequest(BaseModel):
    quantity: int


class ReserveResponse(BaseModel):
    product_id: int
    reserved: int
    remaining: int