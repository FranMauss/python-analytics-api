from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.schemas.player import PlayerCreate, PlayerResponse
from app.services.players import create_player

router = APIRouter(prefix="/players", tags=["Players"])

@router.post("/", response_model=PlayerResponse)
def create(player: PlayerCreate, db: Session = Depends(get_db)):
    try:
        return create_player(db, player.name, player.tier)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
