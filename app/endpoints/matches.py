from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.schemas.match import MatchCreate, MatchResponse
from app.services.matches import create_match

router = APIRouter(prefix="/matches", tags=["Matches"])

@router.post("/", response_model=MatchResponse)
def create(match: MatchCreate, db: Session = Depends(get_db)):
    try:
        return create_match(
            db=db,
            player_a_name=match.player_a_name,
            player_b_name=match.player_b_name,
            tournament_tier=match.tournament_tier,
            date=match.date,
            winner_name=match.winner_name,
            player_b_tier=match.player_b_tier
        )
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
