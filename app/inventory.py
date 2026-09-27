from typing import Optional

from app.models import Product


class ProductNotFound(Exception):
    pass


class InsufficientStock(Exception):
    pass


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

    def reserve(self, product_id: int, quantity: int) -> Product:
        product = self._products.get(product_id)
        if product is None:
            raise ProductNotFound(product_id)
        if quantity > product.stock:
            raise InsufficientStock(product_id)
        product.stock -= quantity
        return product