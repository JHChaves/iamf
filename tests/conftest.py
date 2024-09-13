import pytest
from fastapi.testclient import TestClient

from iamf.app import app


@pytest.fixture
def client():
    return TestClient(app)
