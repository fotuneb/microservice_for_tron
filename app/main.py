from fastapi import FastAPI
from app.api.endpoints.tron import router as tron_router

# Создаем приложение FastAPI
app = FastAPI(
    title="Tron Account Info API",
    description="API для получения информации об адресе в сети Tron, включая баланс, bandwidth и energy.",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json",
)

# Подключаем маршруты
app.include_router(tron_router, prefix="/api", tags=["Tron"])
