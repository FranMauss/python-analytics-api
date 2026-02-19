from sqlalchemy import Column, Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from app.db.base import Base
from datetime import datetime

class EloHistory(Base):
    __tablename__ = "elo_history"

    id = Column(Integer, primary_key=True, index=True)

    player_id = Column(Integer, ForeignKey("players.id"), nullable=False)
    match_id = Column(Integer, ForeignKey("matches.id"), nullable=False)

    elo_before = Column(Integer, nullable=False)
    elo_after = Column(Integer, nullable=False)
    delta = Column(Integer, nullable=False)

    date = Column(DateTime, default=datetime.utcnow)

    player = relationship("Player")
    match = relationship("Match")
