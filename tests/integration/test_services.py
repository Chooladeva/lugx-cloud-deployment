import os
import requests
import pytest

# Read base URLs from environment variables (set in GitHub Actions)
GAMES_URL = os.getenv("BASE_URL_GAMES", "http://app.lugx.cloud/api/games/")
ORDERS_URL = os.getenv("BASE_URL_ORDERS", "http://app.lugx.cloud/api/orders/")
ANALYTICS_URL = os.getenv("BASE_URL_ANALYTICS", "http://app.lugx.cloud/api/analytics/event")

def test_game_service():
    """Check that Game Service API returns 200 OK"""
    r = requests.get(GAMES_URL)
    assert r.status_code == 200

def test_order_service():
    """Check that Order Service API returns 200 OK"""
    r = requests.get(ORDERS_URL)
    assert r.status_code == 200

def test_analytics_service():
    """Check that Analytics Service API returns 200 OK"""
    r = requests.get(ANALYTICS_URL)
    assert r.status_code == 200

