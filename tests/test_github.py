import requests_mock
from app import app


def test_github():
    with app.test_client() as client:
        with requests_mock.Mocker() as mocker:
            mocker.get("https://api.github.com", json={"test": "test"})
            resp = client.get("/api/v1/github")
            assert resp.status_code == 200
            assert resp.json.get("test") == "test"

