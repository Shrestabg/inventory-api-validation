from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_create_product():
    response = client.post(
        "/products", json={"name": "Widget", "price": 9.99, "stock": 10}
    )
    assert response.status_code == 201
    body = response.json()
    assert body["id"] == 1
    assert body["name"] == "Widget"
    assert body["price"] == 9.99
    assert body["stock"] == 10


def test_get_product():
    created = client.post(
        "/products", json={"name": "Gadget", "price": 5.0, "stock": 3}
    ).json()
    response = client.get(f"/products/{created['id']}")
    assert response.status_code == 200
    assert response.json()["name"] == "Gadget"


def test_get_missing_product_returns_404():
    response = client.get("/products/9999")
    assert response.status_code == 404


def test_reserve_reduces_stock():
    created = client.post(
        "/products", json={"name": "Widget", "price": 9.99, "stock": 10}
    ).json()
    response = client.post(f"/products/{created['id']}/reserve", json={"quantity": 3})
    assert response.status_code == 200
    body = response.json()
    assert body["product_id"] == created["id"]
    assert body["reserved"] == 3
    assert body["remaining"] == 7


def test_reserve_more_than_stock_rejected():
    created = client.post(
        "/products", json={"name": "Nail", "price": 0.5, "stock": 4}
    ).json()
    response = client.post(f"/products/{created['id']}/reserve", json={"quantity": 6})
    assert response.status_code == 409


def test_reserve_missing_product_returns_404():
    response = client.post("/products/9999/reserve", json={"quantity": 1})
    assert response.status_code == 404


def test_create_product_rejects_negative_price():
    response = client.post("/products", json={"name": "Bad", "price": -1, "stock": 5})
    assert response.status_code == 422


def test_create_product_rejects_negative_stock():
    response = client.post("/products", json={"name": "Bad", "price": 1, "stock": -5})
    assert response.status_code == 422


def test_create_product_rejects_empty_name():
    response = client.post("/products", json={"name": "", "price": 1, "stock": 5})
    assert response.status_code == 422


def test_reserve_quantity_zero_rejected():
    created = client.post(
        "/products", json={"name": "Screw", "price": 0.3, "stock": 4}
    ).json()
    response = client.post(f"/products/{created['id']}/reserve", json={"quantity": 0})
    assert response.status_code == 422