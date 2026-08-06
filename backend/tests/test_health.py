from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_health_check_returns_ok() -> None:
    """Comprueba que el endpoint de salud responde correctamente."""

    response = client.get("/api/v1/health")

    assert response.status_code == 200
    assert response.json() == {
        "status": "ok",
        "service": "de-mi-tierra-api",
        "version": "0.1.0",
    }