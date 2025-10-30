from http import HTTPStatus

from fastapi.testclient import TestClient

from fast_api_zero.app import app


def test_root_deve_retornar_ola_mundo():
    client = TestClient(app)

    response = client.get("/")

    assert response.json() == {"message": "Olá Mundo"}
    assert response.status_code == HTTPStatus.OK


def test_create_user():
    client = TestClient(app)

    response = client.post(
        "/users",
        json={
            "username": "alice",
            "email": "alice@example.com",
            "password": "securepassword",
        },
    )

    assert response.status_code == HTTPStatus.CREATED
