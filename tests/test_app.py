import sqlite3
from pathlib import Path
from tempfile import NamedTemporaryFile
from unittest.mock import MagicMock, patch

import pytest
from fastapi.testclient import TestClient

from app import app


@pytest.fixture
def client(monkeypatch):
    with NamedTemporaryFile(suffix=".db", delete=False) as database:
        database_path = Path(database.name)

    real_connect = sqlite3.connect

    connection = real_connect(database_path)

    connection.execute(
        """
        CREATE TABLE users (
            id INTEGER PRIMARY KEY,
            username TEXT NOT NULL,
            email TEXT NOT NULL
        )
        """
    )

    connection.executemany(
        "INSERT INTO users (id, username, email) VALUES (?, ?, ?)",
        [
            (1, "alice", "alice@example.com"),
            (2, "bob", "bob@example.com"),
            (3, "charlie", "charlie@example.com"),
        ],
    )

    connection.commit()
    connection.close()

    monkeypatch.setattr(
        "app.sqlite3.connect",
        lambda *args, **kwargs: real_connect(database_path),
    )

    yield TestClient(app)

    database_path.unlink(missing_ok=True)


def test_search_existing_user(client):
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


def test_search_rejects_empty_username(client):
    response = client.get("/users", params={"username": ""})

    assert response.status_code == 422


def test_search_rejects_username_over_50_characters(client):
    long_username = "a" * 51

    response = client.get("/users", params={"username": long_username})

    assert response.status_code == 422


def test_sql_injection_payload_is_safe(client):
    payload = "alice' OR '1'='1"

    response = client.get("/users", params={"username": payload})

    assert response.status_code == 200
    assert response.json() == {"users": []}


def test_search_user_with_mocked_database(client):
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


def test_database_error_returns_generic_message(client, caplog):
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
