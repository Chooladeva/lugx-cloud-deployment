from pydantic import BaseModel
from typing import Optional

class Event(BaseModel):
    event_type: str
    page_url: str
    scroll_depth: Optional[float] = 0.0
    click_target: Optional[str] = ""
    session_id: str
    duration: Optional[int] = 0

