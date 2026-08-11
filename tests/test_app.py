from fastapi.testclient import TestClient

from app import app

client = TestClient(app)


def test_search_existing_user():
    response = client.get("/users", params={"username": "alice"})

    assert response.status_code == 200
    assert response.json() == {
        "users": [
            {
                "id": 1,
                "username": "alice",
                "email": "alice@example.com",
            }
        ]
    }


def test_search_rejects_empty_username():
    response = client.get("/users", params={"username": ""})

    assert response.status_code == 422


def test_search_rejects_username_over_50_characters():
    long_username = "a" * 51

    response = client.get("/users", params={"username": long_username})

    assert response.status_code == 422


def test_sql_injection_payload_is_safe():
    payload = "alice' OR '1'='1"

    response = client.get("/users", params={"username": payload})

    assert response.status_code == 200
    assert response.json() == {"users": []}


from unittest.mock import MagicMock, patch


def test_search_user_with_mocked_database():
    mock_connection = MagicMock()
    mock_connection.execute.return_value.fetchall.return_value = [
        (99, "mock-user", "mock@example.com")
    ]

    with patch("app.sqlite3.connect", return_value=mock_connection):
        response = client.get("/users", params={"username": "mock-user"})

    assert response.status_code == 200
    assert response.json() == {
        "users": [
            {
                "id": 99,
                "username": "mock-user",
                "email": "mock@example.com",
            }
        ]
    }

    mock_connection.execute.assert_called_once_with(
        """
            SELECT id, username, email
            FROM users
            WHERE username = ?
        """,
        ("mock-user",),
    )


import sqlite3


def test_database_error_returns_generic_message(caplog):
    with (
        patch(
            "app.sqlite3.connect",
            side_effect=sqlite3.Error("SECRET DATABASE DETAILS"),
        ),
        caplog.at_level("ERROR"),
    ):
        response = client.get("/users", params={"username": "alice"})

    assert response.status_code == 500
    assert response.json() == {"detail": "Unable to process the request."}

    assert "Database error while searching users" in caplog.text
    assert "SECRET DATABASE DETAILS" in caplog.text
