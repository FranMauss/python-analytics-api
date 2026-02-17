from sqlalchemy import Column, Integer, ForeignKey, Date, CheckConstraint
from sqlalchemy.orm import relationship
from app.core.database import Base

class Match(Base):
    __tablename__ = "matches"

    id = Column(Integer, primary_key=True)
    player_a_id = Column(Integer, ForeignKey("players.id"), nullable=False)
    player_b_id = Column(Integer, ForeignKey("players.id"), nullable=False)
    winner_id = Column(Integer, ForeignKey("players.id"), nullable=True)
    tournament_tier = Column(Integer, nullable=False)
    date = Column(Date, nullable=False)

    player_a = relationship("Player", foreign_keys=[player_a_id])
    player_b = relationship("Player", foreign_keys=[player_b_id])
    winner = relationship("Player", foreign_keys=[winner_id])

    __table_args__ = (
        CheckConstraint("tournament_tier >= 1 AND tournament_tier <= 3", name="check_tournament_tier"),
        CheckConstraint("player_a_id != player_b_id", name="check_distinct_players"),
    )