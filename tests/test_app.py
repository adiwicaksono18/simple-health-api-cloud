from app import app


def test_health_endpoint():
    client = app.test_client()
    response = client.get("/health")

    assert response.status_code == 200
    assert response.get_json() == {"status": "healthy"}
    
def test_home_endpoint():
    client = app.test_client()
    response = client.get("/")
    data = response.get_json()

    assert response.status_code == 200
    assert data["app"] == "Simple Health API"
    assert "Docker" in data["message"]


def test_hello_endpoint():
    client = app.test_client()
    response = client.get("/api/hello/Mahasiswa")
    data = response.get_json()

    assert response.status_code == 200
    assert "Mahasiswa" in data["message"]
