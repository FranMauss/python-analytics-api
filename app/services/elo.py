from app.models.player import Player
from app.models.match import Match
from sqlalchemy.orm import Session

# Logica de +-elo por partida
ELO_TABLE = {
    3: {  # Torneo tier 3
        4: {"win": 5, "lose": -45},
        3: {"win": 15, "lose": -35},
        2: {"win": 25, "lose": -25},
        1: {"win": 35, "lose": -15},
    },
    2: {  # Torneo tier 2
        4: {"win": 20, "lose": -80},
        3: {"win": 35, "lose": -65},
        2: {"win": 50, "lose": -50},
        1: {"win": 75, "lose": -25},
    },
    1: {  # Torneo tier 1
        4: {"win": 40, "lose": -160},
        3: {"win": 75, "lose": -125},
        2: {"win": 100, "lose": -100},
        1: {"win": 150, "lose": -50},
    },
}

def calculate_elo_change(player: Player, opponent: Player, did_win: bool, tournament_tier: int) -> int:

    if did_win:
        return ELO_TABLE[tournament_tier][opponent.tier]["win"]
    else:
        return ELO_TABLE[tournament_tier][opponent.tier]["lose"]

def apply_elo_to_match(match: Match, db: Session):
    """
    Solo cambia elo de players internos, empates no afectan
    """
    # primero checkeamos si hay empate
    if match.winner_id is None:
        return

    player_a = match.player_a
    player_b = match.player_b

    if match.winner_id == match.player_a_id:
        result_a = True
        result_b = False
    else:
        result_a = False
        result_b = True

    # Se cambia el elo solo a internos

    if not player_a.is_external:
        points_a = calculate_elo_change(player_a, player_b, result_a, match.tournament_tier)
        player_a.elo += points_a

    if not player_b.is_external:
        points_b = calculate_elo_change(player_b, player_a, result_b , match.tournament_tier)
        player_b.elo += points_b


    db.commit()
