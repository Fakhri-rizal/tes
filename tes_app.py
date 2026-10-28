from app import app

def test_login_route_exists():
    client = app.test_client()
    response = client.get("/login?username=admin&password=test")
    assert response.status_code == 200