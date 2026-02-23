from app.config.settings import settings
import os
import uvicorn


if __name__ == "__main__":
    MAX_WORKERS = os.cpu_count()
    uvicorn.run(
        "app.main:app",
        host=settings.host,
        port=settings.port,
        reload=settings.debug,
        workers=MAX_WORKERS,
        log_level="info",
        access_log=False,
        use_colors=True,
    )
