from app.core.database import Base, engine
from app.models.player import Player
from app.models.match import Match
from app.models.elo_history import EloHistory

def init_db():
    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    init_db()
