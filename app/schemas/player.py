from pydantic import BaseModel

# -------- INPUT --------
class PlayerCreate(BaseModel):
    name: str
    tier: int


# -------- OUTPUT --------
class PlayerResponse(BaseModel):
    id: int
    name: str
    tier: int
    is_external: bool
    elo: int

    class Config:
        orm_mode = True
