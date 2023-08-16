from conftest import client
from modules.fixtures.db import test_db


def test_signup(test_db):
    # Prepare user data
    user_data = {
        "first_name": "testuser",
        "last_name": "testuser",
        "email": "test@example.com",
        "password": "testpassword",
    }

    # Make signup request
    response = client.post("/api/auth/signup", json=user_data)
    assert response.status_code == 200
    assert "id" in response.json()
    assert response.json()["email"] == user_data.get("email")
