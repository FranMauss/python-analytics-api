from sqlalchemy.orm import Session
from app.models.player import Player
from app.models.match import Match
from app.utils.normalization import normalize_name
from app.services.elo import apply_elo_to_match

def create_match(
    db: Session,
    player_a_name: str,
    player_b_name: str,
    tournament_tier: int,
    date,
    winner_name: str | None,
    player_b_tier: int | None
):
    player_a = db.query(Player).filter(
        Player.name_normalized == normalize_name(player_a_name)
    ).first()

    if not player_a:
        raise ValueError("Player A does not exist")

    player_b = db.query(Player).filter(
        Player.name_normalized == normalize_name(player_b_name)
    ).first()

    if not player_b:
        if player_b_tier is None:
            raise ValueError("player_b_tier is required")

        player_b = Player(
            name=player_b_name,
            name_normalized=normalize_name(player_b_name),
            tier=player_b_tier,
            is_external=True
        )
        db.add(player_b)
        db.commit()
        db.refresh(player_b)

    winner_id = None
    if winner_name:
        winner = db.query(Player).filter(
            Player.name_normalized == normalize_name(winner_name)
        ).first()

        if not winner or winner.id not in [player_a.id, player_b.id]:
            raise ValueError("Winner must be Player A or B")

        winner_id = winner.id

    match = Match(
        player_a_id=player_a.id,
        player_b_id=player_b.id,
        winner_id=winner_id,
        tournament_tier=tournament_tier,
        date=date
    )


    db.add(match)
    db.commit()
    db.refresh(match)
    apply_elo_to_match(match, db)


    return match
