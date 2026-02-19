from pydantic import BaseModel
from datetime import datetime

class EloHistoryItem(BaseModel):
    match_id: int
    elo_before: int
    elo_after: int
    delta: int
    date: datetime

    class Config:
        from_attributes = True
