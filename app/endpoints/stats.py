from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.services.stats import get_internal_players_stats
from app.schemas.stats import PlayerStatsResponse
from typing import Dict

router = APIRouter(prefix="/stats", tags=["Stats"])

@router.get("/players", response_model=Dict[str, PlayerStatsResponse])

def stats_players(db: Session = Depends(get_db)):
    return get_internal_players_stats(db)

