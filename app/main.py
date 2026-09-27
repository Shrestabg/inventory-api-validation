from fastapi import FastAPI

app = FastAPI(title="Inventory API")


@app.get("/health")
def health() -> dict:
    return {"status": "ok"}