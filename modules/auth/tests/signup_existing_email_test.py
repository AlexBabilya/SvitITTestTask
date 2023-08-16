from conftest import client
from modules.user.models import User
from modules.fixtures.db import test_db


def test_signup_existing_email(test_db):
    # Create a user with the same email
    existing_user = User(hashed_password="existinguser", email="test@example.com")
    test_db.add(existing_user)
    test_db.commit()

    # Prepare user data with existing email
    user_data = {
        "first_name": "testuser",
        "last_name": "testuser",
        "email": "test@example.com",
        "password": "testpassword",
    }
    # Make signup request
    response = client.post("/api/auth/signup", json=user_data)
    assert response.status_code == 400
