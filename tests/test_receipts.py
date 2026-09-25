import io

import pytest

from app import create_app


@pytest.fixture
def client():
    return create_app().test_client()


def test_post_image_returns_line_items(client):
    data = {"image": (io.BytesIO(b"fake image bytes"), "receipt.jpg")}
    resp = client.post("/receipts", data=data, content_type="multipart/form-data")
    assert resp.status_code == 200
    body = resp.get_json()
    assert body["line_items"]
    for item in body["line_items"]:
        assert {"name", "quantity", "price"} <= item.keys()


def test_missing_image_is_400(client):
    resp = client.post("/receipts")
    assert resp.status_code == 400
    assert "error" in resp.get_json()
