import pytest
from app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True

    with app.test_client() as client:
        yield client


def test_health_check(client):
    response = client.get("/health")

    assert response.status_code == 200
    assert response.get_json()["status"] == "ok"


def test_public_document_access(client):
    response = client.get("/document/1")

    assert response.status_code == 200
    assert response.get_json()["title"] == "Company Overview"


def test_internal_document_access_denied(client):
    response = client.get("/document/3")

    assert response.status_code == 403


def test_nonexistent_document(client):
    response = client.get("/document/999")

    assert response.status_code == 404


def test_search_returns_public_documents(client):
    response = client.get("/search?q=security")

    assert response.status_code == 200

    results = response.get_json()["results"]

    assert len(results) > 0
    assert all(doc["owner"] == "public" for doc in results)


def test_search_does_not_expose_internal_audit(client):
    response = client.get("/search?q=internal")

    assert response.status_code == 200
    assert response.get_json()["results"] == []
def test_security_headers(client):
    response = client.get("/")

    assert response.status_code == 200
    assert response.headers["X-Content-Type-Options"] == "nosniff"
    assert response.headers["X-Frame-Options"] == "SAMEORIGIN"
    assert response.headers["Content-Security-Policy"] == "default-src 'self'"
    assert response.headers["Referrer-Policy"] == "strict-origin-when-cross-origin"


def test_health_security_headers(client):
    response = client.get("/health")

    assert response.status_code == 200
    assert response.headers["X-Content-Type-Options"] == "nosniff"
    assert response.headers["X-Frame-Options"] == "SAMEORIGIN"
    assert response.headers["Content-Security-Policy"] == "default-src 'self'"
    assert response.headers["Referrer-Policy"] == "strict-origin-when-cross-origin"
