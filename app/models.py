from pydantic import BaseModel, Field


class Product(BaseModel):
    id: int
    name: str
    price: float
    stock: int


class ProductCreate(BaseModel):
    name: str = Field(..., min_length=1)
    price: float = Field(..., gt=0)
    stock: int = Field(..., ge=0)


class ReserveRequest(BaseModel):
    quantity: int = Field(..., gt=0)


class ReserveResponse(BaseModel):
    product_id: int
    reserved: int
    remaining: int