from app import app

def test_home_status_code():
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200

def test_home_content():
    client = app.test_client()
    response = client.get('/')
    assert b"Hello" in response.data

def test_health_check():
    client = app.test_client()
    response = client.get('/health')
    assert response.status_code == 200