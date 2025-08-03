import requests
from .schemas import Event

CLICKHOUSE_URL = "http://clickhouse:8123"
TABLE_NAME = "web_events"

def insert_event(event: Event):
    query = f"INSERT INTO {TABLE_NAME} (event_type, page_url, scroll_depth, click_target, session_id, duration) FORMAT JSONEachRow"
    payload = event.dict()
    
    payload.pop("timestamp", None)

    response = requests.post(
        f"{CLICKHOUSE_URL}/?query={query}",
        json=[payload],
        headers={"Content-Type": "application/json"}
    )

    if response.status_code != 200:
        raise Exception(f"ClickHouse insert failed: {response.status_code} - {response.text}")
