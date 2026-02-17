from pydantic import BaseModel, conint
from typing import Optional
from datetime import date

class MatchCreate(BaseModel):
    player_a_name: str
    player_b_name: str
    player_b_tier: Optional[conint(ge=1, le=4)] = None
    winner_name: Optional[str] = None
    tournament_tier: conint(ge=1, le=3)
    date: date

class MatchResponse(BaseModel):
    id: int
    player_a_id: int
    player_b_id: int
    winner_id: Optional[int]
    tournament_tier: int
    date: date

    class Config:
        orm_mode = True