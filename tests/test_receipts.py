import pytest
from fastapi.testclient import TestClient

from app import app


@pytest.fixture
def client():
    return TestClient(app)


def test_post_image_returns_line_items(client):
    files = {"image": ("receipt.jpg", b"fake image bytes", "image/jpeg")}
    resp = client.post("/receipts", files=files)
    assert resp.status_code == 200
    body = resp.json()
    assert body["line_items"]
    for item in body["line_items"]:
        assert {"name", "quantity", "price"} <= item.keys()


def test_missing_image_is_422(client):
    resp = client.post("/receipts")
    assert resp.status_code == 422
