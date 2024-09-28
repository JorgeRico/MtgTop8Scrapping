from pydantic import BaseModel
from models.card import TopCard
from models.player import PlayerStats

class TournamentStats(BaseModel):
    top10 : list[TopCard] 
    mb    : list[TopCard] 
    sb    : list[TopCard] 

class LeagueStats(BaseModel):
    top20   : list[TopCard] 
    mb      : list[TopCard] 
    sb      : list[TopCard] 
    players : list[PlayerStats]