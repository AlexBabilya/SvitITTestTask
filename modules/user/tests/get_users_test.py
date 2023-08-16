from conftest import client
from modules.user.crud import create_user
from modules.user.schemas import UserCreate
from modules.fixtures.db import test_db


def test_read_users(test_db):
    # Create test user data
    print(test_db)
    user_data = UserCreate(
        email="test@example.com",
        password="testpassword",
        first_name="test",
        last_name="test",
    )
    create_user(test_db, user_data)

    response = client.get("/api/users/")
    assert response.status_code == 200
    assert len(response.json()) == 1
