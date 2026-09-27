from fastapi import FastAPI, HTTPException

from app.inventory import InventoryStore
from app.models import Product, ProductCreate

app = FastAPI(title="Inventory API")
inventory = InventoryStore()


@app.get("/health")
def health() -> dict:
    return {"status": "ok"}


@app.get("/products/{product_id}")
def get_product(product_id: int) -> Product:
    product = inventory.get_product(product_id)
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return product


@app.post("/products", status_code=201)
def create_product(payload: ProductCreate) -> Product:
    return inventory.create_product(payload.name, payload.price, payload.stock)