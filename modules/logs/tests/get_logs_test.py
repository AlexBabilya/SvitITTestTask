import pytest

from conftest import client
from modules.logs.models import LogEntry
from modules.auth.utils import create_access_token
from modules.user.models import User
from modules.fixtures.db import test_db


@pytest.fixture
def test_user(test_db):
    user = User(hashed_password="testuser", email="test@example.com")
    test_db.add(user)
    test_db.commit()
    return user


@pytest.fixture
def test_token(test_user):
    return create_access_token(data={"sub": test_user.email})


def test_get_logs(test_db, test_token):
    # Create some sample log entries in the database
    log_entries = [LogEntry(message="Log entry 1"), LogEntry(message="Log entry 2")]
    test_db.add_all(log_entries)
    test_db.commit()

    headers = {"Authorization": f"Bearer {test_token}"}
    response = client.get("/api/logs/", headers=headers)
    assert response.status_code == 200

    # Check if the response contains the expected log entries
    returned_logs = response.json()
    assert len(returned_logs) == 2
    assert returned_logs[0]["message"] == "Log entry 1"
    assert returned_logs[1]["message"] == "Log entry 2"
