from pydantic import BaseModel
from models.card import Card

class Player(BaseModel):
    id       : int 
    name     : str
    position : int
    idDeck   : int

class PlayerData(BaseModel):
    id       : int 
    name     : str
    position : int
    idDeck   : int
    deck     : list[Card]
