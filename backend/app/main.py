from fastapi import FastAPI

from app.api.routes.health import router as health_router


def create_application() -> FastAPI:
    """Crea y configura la aplicación FastAPI."""

    application = FastAPI(
        title="DeMiTierra API",
        description="API backend del marketplace DeMiTierra.",
        version="0.1.0",
    )

    application.include_router(
        health_router,
        prefix="/api/v1",
    )

    return application


app = create_application()