"""Local portfolio API. Demo mode never opens an external database connection."""
from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers.calculation import router as calculation_router
from app.routers.live_tags import router as live_tags_router
from app.routers.prediction import router as prediction_router
from app.services.auto_calculation import AutoCalculation

@asynccontextmanager
async def lifespan(app):
    worker = AutoCalculation()
    worker.start()
    try:
        yield
    finally:
        worker.stop()

app = FastAPI(title='Heat Exchanger Optimizer — Portfolio Demo', lifespan=lifespan)
app.add_middleware(CORSMiddleware, allow_origin_regex=r'^http://(localhost|127\.0\.0\.1):5501$',
    allow_methods=['GET','POST','DELETE'], allow_headers=['Content-Type'])
app.include_router(calculation_router)
app.include_router(live_tags_router)
app.include_router(prediction_router)

@app.get('/')
def home():
    from app.database.config import DEMO_MODE
    return {'message':'Heat Exchanger Optimizer', 'demo_mode':DEMO_MODE}
