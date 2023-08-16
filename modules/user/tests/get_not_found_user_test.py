from conftest import client
from modules.fixtures.db import test_db


def test_read_user_not_found(test_db):
    response = client.get("/api/users/123")
    assert response.status_code == 404
    assert "detail" in response.json()
