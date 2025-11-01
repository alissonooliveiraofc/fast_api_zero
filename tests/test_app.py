from http import HTTPStatus


def test_root_deve_retornar_ola_mundo(client):
    response = client.get("/")

    assert response.json() == {"message": "Olá Mundo"}
    assert response.status_code == HTTPStatus.OK


def test_create_user(client):
    response = client.post(
        "/users",
        json={
            "username": "alice",
            "email": "alice@example.com",
            "password": "securepassword",
        },
    )

    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        "id": 1,
        "username": "alice",
        "email": "alice@example.com",
    }


def test_read_users(client):
    response = client.get("/users")

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        "users": [
            {
                "id": 1,
                "username": "alice",
                "email": "alice@example.com",
            }
        ]
    }


def test_update_user(client):
    response = client.put(
        "/users/1",
        json={
            "username": "sheldon cooper",
            "email": "sheldon@bazinga.com",
            "password": "bazinga123",
        },
    )

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        "id": 1,
        "username": "sheldon cooper",
        "email": "sheldon@bazinga.com",
    }


def test_delete_user(client):
    response = client.delete("/users/1")

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        "id": 1,
        "username": "sheldon cooper",
        "email": "sheldon@bazinga.com",
    }
