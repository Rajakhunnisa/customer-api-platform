from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_and_get_customer():
    response = client.post("/customers/", json={
        "first_name": "John",
        "middle_name": "M",
        "last_name": "Doe",
        "email": "john@example.com",
        "phone_number": "123-456-7890"
    })
    assert response.status_code == 200
    data = response.json()
    assert data["email"] == "john@example.com"