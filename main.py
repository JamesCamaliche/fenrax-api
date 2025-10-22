from fastapi import FastAPI

app = FastAPI(title="Fenrax API")

@app.get("/")
def root():
    return {"status": "Fenrax API is live"}

@app.get("/health")
def health():
    return {"ok": True}
