import pytest
from fastapi.testclient import TestClient

from app import database
from app.main import app


@pytest.fixture(autouse=True)
def reset_database():
    database.reset()
    yield
    database.reset()


@pytest.fixture
def client():
    with TestClient(app) as test_client:
        yield test_client
