from conftest import client
from modules.user.crud import create_user
from modules.user.schemas import UserCreate
from modules.fixtures.db import test_db


def test_read_user(test_db):
    # Create test user data

    user_data = UserCreate(
        email="test@example.com",
        password="testpassword",
        first_name="test",
        last_name="test",
    )
    created_user = create_user(test_db, user_data)

    response = client.get(f"/api/users/{created_user.id}")
    assert response.status_code == 200
    assert response.json()["id"] == created_user.id
    assert response.json()["email"] == created_user.email
