from sqlalchemy import Column, Integer, ForeignKey, DateTime
from sqlalchemy.sql import func
from app.core.database import Base

class EloHistory(Base):
    __tablename__ = "elo_history"

    id = Column(Integer, primary_key=True, index=True)
    player_id = Column(Integer, ForeignKey("players.id"), nullable=False)
    match_id = Column(Integer, ForeignKey("matches.id"), nullable=True)
    elo_before = Column(Integer, nullable=False)
    elo_after = Column(Integer, nullable=False)
    timestamp = Column(DateTime(timezone=True), server_default=func.now())
