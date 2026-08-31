from pathlib import Path

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from app.routers.calculation import router as calculation_router
from app.routers.login import router as login_router
from app.routers.live_tags import router as live_tags_router

app = FastAPI(
    title="Heat Exchanger Cleaning Optimizer API",
    description="API for heat-exchanger performance calculations and monitoring.",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5500",
        "http://127.0.0.1:5500"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(calculation_router, prefix="/api", tags=["calculations"])
app.include_router(login_router, prefix="/api", tags=["authentication"])
app.include_router(live_tags_router, prefix="/api", tags=["monitoring"])

@app.get("/api/health", tags=["health"])
def health_check():
    return {
        "status": "ok",
        "message": "Heat Exchanger Backend is Running!",
    }

frontend_directory = Path(__file__).resolve().parents[2] / "frontend"
app.mount("/", StaticFiles(directory=frontend_directory, html=True), name="frontend")
