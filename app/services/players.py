from sqlalchemy.orm import Session
from app.models.player import Player
from app.utils.normalization import normalize_name

def create_player(db: Session, name: str, tier: int):
    normalized_name = normalize_name(name)

    existing = db.query(Player).filter(
        Player.name_normalized == normalized_name
    ).first()

    if existing:
        raise ValueError("Player already exists")

    player = Player(
        name=name,
        name_normalized=normalized_name,
        tier=tier,
        is_external=False
    )

    db.add(player)
    db.commit()
    db.refresh(player)

    return player
