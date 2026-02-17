from sqlalchemy import Column, Integer, String, Boolean, CheckConstraint
from app.core.database import Base

class Player(Base):
    __tablename__ = "players"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    name_normalized = Column(String, unique=True, index=True, nullable=False)
    tier = Column(Integer, nullable=False)
    is_external = Column(Boolean, default=False)
    elo = Column(Integer, default=2000)

    __table_args__ = (
        CheckConstraint("tier >= 1 AND tier <= 4", name="check_player_tier"),
    )