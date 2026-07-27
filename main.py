from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import os

app = FastAPI(
    title="Neenaam Platform",
    version="2.0.3"
)

if os.path.exists("static"):
    app.mount("/static", StaticFiles(directory="static"), name="static")

class SearchPayload(BaseModel):
    query: str

@app.get("/", response_class=HTMLResponse)
async def serve_root():
    index_path = "static/index.html"
    if os.path.exists(index_path):
        with open(index_path, "r", encoding="utf-8") as f:
            return f.read()
    return "<h3>Neenaam Platform is active. Please ensure static/index.html is deployed.</h3>"

@app.post("/api/deep-search")
async def execute_deep_search(payload: SearchPayload):
    query = payload.query
    return {
        "status": "success",
        "queryId": "neenaam_q_99281",
        "generatedScript": f"التحليل والاستخراج للمحتوى:\n\"{query}\"",
        "executionTimeMs": 150.0
    }
