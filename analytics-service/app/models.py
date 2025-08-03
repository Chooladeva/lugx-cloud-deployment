import requests

CLICKHOUSE_URL = "http://clickhouse:8123"
TABLE_NAME = "web_events"

def create_table():
    ddl = f"""
    CREATE TABLE IF NOT EXISTS {TABLE_NAME} (
        event_type String,
        page_url String,
        scroll_depth Float64,
        click_target String,
        session_id String,
        duration Int32,
        timestamp DateTime DEFAULT now()
    ) ENGINE = MergeTree()
    ORDER BY (event_type, timestamp)
    """
    response = requests.post(f"{CLICKHOUSE_URL}/?query={ddl}")
    if response.status_code != 200:
        raise Exception(f"Failed to create table: {response.text}")

