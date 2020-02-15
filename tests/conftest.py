from app import create_app
from config import TestingConfig
import pytest

app = create_app(TestingConfig)

@pytest.fixture
def client(tmpdir):
    with app.test_client() as c:
        yield c