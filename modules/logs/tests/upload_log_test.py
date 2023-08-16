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


def test_upload_logs(test_db, test_token):
    # Prepare a log file and upload it
    log_data = "Log entry 1\nLog entry 2\n"
    files = {"file": ("log.txt", log_data, "text/plain")}
    headers = {"Authorization": f"Bearer {test_token}"}
    response = client.post("/api/logs/upload", files=files, headers=headers)
    assert response.status_code == 200
    assert response.json() == {"message": "Logs uploaded successfully"}

    # Check if log entries were added to the database
    db_logs = test_db.query(LogEntry).all()
    assert len(db_logs) == 2
