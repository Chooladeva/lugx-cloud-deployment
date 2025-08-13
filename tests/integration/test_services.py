import requests

# Port-forwarded endpoints for inactive pods in CI/CD workflow
GAME_URL = "http://localhost:8001/api/games/"
ORDER_URL = "http://localhost:8002/api/orders/"
ANALYTICS_URL = "http://localhost:8003/api/analytics/event"

def test_game_service():
    """Check that Game Service API returns 200 OK"""
    r = requests.get(GAME_URL)
    assert r.status_code == 200, f"Game Service failed with status {r.status_code}"

def test_order_service():
    """Check that Order Service API returns 200 OK"""
    r = requests.get(ORDER_URL)
    assert r.status_code == 200, f"Order Service failed with status {r.status_code}"

def test_analytics_service():
    """Check that Analytics Service API returns 200 OK"""
    r = requests.get(ANALYTICS_URL)
    assert r.status_code == 200, f"Analytics Service failed with status {r.status_code}"
