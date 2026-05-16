import pytest
from app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_health_endpoint(client):
    response = client.get("/api/health")
    assert response.status_code == 200
    data = response.get_json()
    assert data["status"] == "ok"

def test_generate_hybrid_endpoint(client):
    response = client.post("/api/generate", json={"mode": "hybrid", "words": 4})
    assert response.status_code == 200
    data = response.get_json()
    assert "passphrase" in data
    assert "entropy" in data

def test_benchmark_endpoint(client):
    response = client.post("/api/benchmark", json={"mode": "hybrid", "count": 10})
    assert response.status_code == 200
    data = response.get_json()
    assert data["count"] == 10
    assert "generation_time_sec" in data
