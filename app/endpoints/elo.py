from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.models.elo_history import EloHistory
from app.schemas.elo import EloHistoryItem

router = APIRouter(prefix="/elo", tags=["Elo"])

@router.get("/players/{player_id}/history", response_model=list[EloHistoryItem])
def get_elo_history(player_id: int, db: Session = Depends(get_db)):
    history = (
        db.query(EloHistory)
        .filter(EloHistory.player_id == player_id)
        .order_by(EloHistory.date.asc())
        .all()
    )
    return history
