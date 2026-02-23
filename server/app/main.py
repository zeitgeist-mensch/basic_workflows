from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.controllers.health_controller import router as health_router
from app.middlewares.request_logger import request_logging_middleware
from app.config.settings import settings

app = FastAPI(
    title=settings.app_name,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.middleware("http")(request_logging_middleware)

app.include_router(health_router)
