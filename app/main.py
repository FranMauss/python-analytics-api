from fastapi import FastAPI
from app.endpoints import players, matches, stats

app = FastAPI(title="Magic Analytics API")

app.include_router(players.router, prefix="/players", tags=["Players"])
app.include_router(matches.router, prefix="/matches", tags=["Matches"])
app.include_router(stats.router, prefix="/stats", tags=["Stats"])


