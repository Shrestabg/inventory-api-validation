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