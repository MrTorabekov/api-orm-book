from main import app
from starlette.testclient import TestClient

client = TestClient(app)


def test_information():
    response = client.get("/info")
    assert response.status_code == 200
    assert response.json() == {"message":"hello world"}