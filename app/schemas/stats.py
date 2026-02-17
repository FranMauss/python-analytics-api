from pydantic import BaseModel, Field
from typing import Dict

class PlayerInfo(BaseModel):
    id: int
    name: str
    tier: int
    elo: int

class WinStats(BaseModel):
    wins: int
    draws: int
    losses: int
    winrate: float

class VsStats(BaseModel):
    total: WinStats
    by_tier: Dict[int, WinStats]

class PlayerStatsResponse(BaseModel):
    player: PlayerInfo
    global_stats: WinStats = Field(alias="global")
    by_tournament_tier: Dict[int, WinStats]
    vs_internal: VsStats
    vs_external: VsStats

    class Config:
        orm_mode = True
