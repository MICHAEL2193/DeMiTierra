from fastapi import APIRouter

router = APIRouter(tags=["Health"])


@router.get(
    "/health",
    summary="Comprobar el estado de la API",
)
async def health_check() -> dict[str, str]:
    """Devuelve el estado básico del servicio."""

    return {
        "status": "ok",
        "service": "de-mi-tierra-api",
        "version": "0.1.0",
    }