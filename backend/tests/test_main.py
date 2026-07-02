from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_home_returns_html_content():
    response = client.get("/")
    assert response.status_code == 200
    assert "AI Document Assistant" in response.text
