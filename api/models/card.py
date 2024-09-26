from pydantic import BaseModel

MAINDECK_CARD  = "md"
SIDEBOARD_CARD = "sb"

class Card(BaseModel):
    id    : int 
    name  : str
    num   : int
    board : str

class TopCard(BaseModel):
    num  : int 
    name : str