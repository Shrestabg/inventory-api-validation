# inventory-api-validation

A small FastAPI inventory service used as a validation fixture for
Codebase ICU. It provides a minimal in-memory product catalog with
health, product, and reservation endpoints.

## What it does

The service exposes a tiny REST API over an in-memory product store:

| Method | Path                             | Description                      |
| ------ | -------------------------------- | -------------------------------- |
| GET    | `/health`                        | Service health check             |
| POST   | `/products`                      | Create a product                 |
| GET    | `/products/{product_id}`         | Fetch a single product           |
| POST   | `/products/{product_id}/reserve` | Reserve a quantity of a product  |

Reservations reduce the available stock. A product with insufficient
stock cannot be reserved.

## Install dependencies

```bash
pip install -r requirements.txt
```

## Run the service

```bash
uvicorn app.main:app --reload
```

## Run the tests

```bash
pytest -q
```

## Validation state

> **IMPORTANT:** This repository is intentionally in a **regressed
> validation state**. It is a fixture for exercising Codebase ICU, not a
> healthy production service.

A regression has been deliberately introduced and left in place. Two tests
in the suite currently fail:

- `test_reserve_full_stock_is_allowed`
- `test_reserve_all_then_more_fails`

The regression was introduced in a dedicated commit and is discoverable
through the failing tests, the source code, and the Git history. To restore
a clean state, locate the introducing commit, identify the faulty behavior,
and apply a minimal repair. Do not treat the current failure output as the
intended behavior.

All other tests pass. The full suite is expected to be green after the
repair.

## Structure

```
app/
  main.py         FastAPI application and routes
  inventory.py    In-memory store and reservation logic
  models.py       Pydantic models and input validation
tests/
  test_inventory.py
requirements.txt
```