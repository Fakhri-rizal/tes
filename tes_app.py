from app import app

def test_index_route():
    """Memastikan halaman utama dapat diakses."""
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200