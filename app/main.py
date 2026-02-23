from fastapi import FastAPI
from app.endpoints import players, matches, stats, elo

app = FastAPI(title="Magic Analytics API")

app.include_router(players.router, tags=["Players"])
app.include_router(matches.router, tags=["Matches"])
app.include_router(stats.router, tags=["Stats"])
app.include_router(elo.router,tags=["Elo"])