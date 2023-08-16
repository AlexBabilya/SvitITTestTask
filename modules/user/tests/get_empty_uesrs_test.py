from conftest import client
from modules.fixtures.db import test_db


def test_read_users_empty(test_db):
    response = client.get("/api/users/")
    assert response.status_code == 200
    assert response.json() == []
