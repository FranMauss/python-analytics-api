from sqlalchemy.orm import Session
from app.models.player import Player
from app.models.match import Match


def calc_winrate(block: dict) -> float:
    wins = block["wins"]
    draws = block["draws"]
    losses = block["losses"]

    total = wins + draws + losses
    if total == 0:
        return 0.0

    return round((wins / total)*100, 2)


def base_block():
    return {"wins": 0, "draws": 0, "losses": 0, "winrate": 0.0}


def get_internal_players_stats(db: Session):

    internal_players = db.query(Player).filter(Player.is_external == False).all()
    matches = db.query(Match).all()

    result = {}

    for player in internal_players:

        player_id = player.id

        stats = {
            "player": {
                "id": player.id,
                "name": player.name,
                "tier": player.tier,
                "elo": player.elo
            },

            "global": base_block(),

            "by_tournament_tier": {
                1: base_block(),
                2: base_block(),
                3: base_block(),
            },

            "vs_internal": {
                "total": base_block(),
                "by_tier": {
                    1: base_block(),
                    2: base_block(),
                    3: base_block(),
                    4: base_block(),
                }
            },

            "vs_external": {
                "total": base_block(),
                "by_tier": {
                    1: base_block(),
                    2: base_block(),
                    3: base_block(),
                    4: base_block(),
                }
            }
        }

        for match in matches:

            if player_id not in (match.player_a_id, match.player_b_id):
                continue

            if match.player_a_id == player_id:
                rival_id = match.player_b_id
            else:
                rival_id = match.player_a_id

            rival = db.query(Player).filter(Player.id == rival_id).first()

            if match.winner_id == player_id:
                result_key = "wins"
            elif match.winner_id == rival_id:
                result_key = "losses"
            else:
                result_key = "draws"

            # total
            stats["global"][result_key] += 1

            # Por torneo
            t_tier = match.tournament_tier
            stats["by_tournament_tier"][t_tier][result_key] += 1

            # Internal / External
            if rival.is_external:
                side = "vs_external"
            else:
                side = "vs_internal"

            stats[side]["total"][result_key] += 1

            # Por rival
            r_tier = rival.tier
            stats[side]["by_tier"][r_tier][result_key] += 1


        stats["global"]["winrate"] = calc_winrate(stats["global"])

        for tier in stats["by_tournament_tier"]:
            block = stats["by_tournament_tier"][tier]
            block["winrate"] = calc_winrate(block)

        stats["vs_internal"]["total"]["winrate"] = calc_winrate(stats["vs_internal"]["total"])
        for tier in stats["vs_internal"]["by_tier"]:
            block = stats["vs_internal"]["by_tier"][tier]
            block["winrate"] = calc_winrate(block)

        stats["vs_external"]["total"]["winrate"] = calc_winrate(stats["vs_external"]["total"])
        for tier in stats["vs_external"]["by_tier"]:
            block = stats["vs_external"]["by_tier"][tier]
            block["winrate"] = calc_winrate(block)

        result[player.name] = stats

    return result