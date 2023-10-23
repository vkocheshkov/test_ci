from starlette.testclient import TestClient

from poetry_project.main import app
from poetry_project.settings import settings


def test_answer():
    client = TestClient(app)
    result = client.get(settings.main_url)
    assert result.status_code == 200
    assert result.json() == {"status": "ok"}
