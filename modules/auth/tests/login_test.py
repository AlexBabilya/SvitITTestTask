from conftest import client
from modules.user.schemas import UserCreate
from modules.user.crud import create_user
from modules.fixtures.db import test_db


def test_login(test_db):
    # Prepare user data

    user_data = UserCreate(
        first_name="testuser",
        last_name="testuser",
        email="test@example.com",
        password="testpassword",
    )
    create_user(test_db, user_data)

    # Make login request
    login_data = {"username": "test@example.com", "password": "testpassword"}
    response = client.post("/api/auth/login", json=login_data)
    assert response.status_code == 200
    assert "access_token" in response.json()
    assert response.json()["token_type"] == "bearer"
