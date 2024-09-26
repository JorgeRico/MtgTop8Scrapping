from pydantic import BaseModel
from models.player import PlayerData

class Tournament(BaseModel):
    id   : int
    name : str
    date : str

class TournamentData(BaseModel):
    tournament : Tournament
    players    : list[PlayerData]