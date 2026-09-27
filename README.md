# inventory-api-validation

A small FastAPI inventory service used as a validation fixture for
Codebase ICU. It provides a minimal in-memory product catalog with
health, product, and reservation endpoints.

## Getting started

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Run the test suite:

```bash
pytest -q
```

## Endpoints

| Method | Path                             | Description                      |
| ------ | -------------------------------- | -------------------------------- |
| GET    | `/health`                        | Service health check             |
| POST   | `/products`                      | Create a product                 |
| GET    | `/products/{product_id}`         | Fetch a single product           |
| POST   | `/products/{product_id}/reserve` | Reserve a quantity of a product  |