from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the OTPless User Analytics API!"}

def test_signup_counts():
    response = client.get("/metrics/signups")
    assert response.status_code == 200
    assert isinstance(response.json(), dict)

def test_active_users():
    response = client.get("/metrics/active-users")
    assert response.status_code == 200
    assert "active_users" in response.json()

def test_churned_users():
    response = client.get("/metrics/churned-users")
    assert response.status_code == 200
    assert "churned_users" in response.json()

def test_daily_active_users():
    response = client.get("/metrics/daily-active-users")
    assert response.status_code == 200
    assert isinstance(response.json(), dict)
