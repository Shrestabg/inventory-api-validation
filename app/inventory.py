from typing import Optional

from app.models import Product


class InventoryStore:
    def __init__(self) -> None:
        self._products: dict[int, Product] = {}
        self._next_id = 1

    def create_product(self, name: str, price: float, stock: int) -> Product:
        product = Product(id=self._next_id, name=name, price=price, stock=stock)
        self._products[product.id] = product
        self._next_id += 1
        return product

    def get_product(self, product_id: int) -> Optional[Product]:
        return self._products.get(product_id)