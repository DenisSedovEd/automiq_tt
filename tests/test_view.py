from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_index_page():
    response = client.get("/api/")
    assert response.status_code == 200
    assert "text/html" in response.headers["content-type"]


def test_change_page():
    response = client.post(
        "/api/change",
        data={
            "change_list": "CCBBAA",
            "perm_rule": "ABC",
        },
    )
    assert response.status_code == 200
    assert "AABBCC" in response.content.decode("utf8")
