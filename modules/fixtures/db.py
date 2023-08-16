import pytest

from modules.database import Base
from conftest import engine, TestingSessionLocal


@pytest.fixture()
def test_db():
    try:
        db = TestingSessionLocal()
        Base.metadata.create_all(bind=engine)
        yield db
    finally:
        Base.metadata.drop_all(bind=engine)

        db.close()
