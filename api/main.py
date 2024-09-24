from fastapi import FastAPI
from db import Db

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World !!!!"}


@app.get("/leagues/{id}/tournaments")
async def getLeague(id):
    db     = Db()
    conn   = db.connect()

    query  = 'Select id, name, date from tournament where idLeague = ' + id
    result = db.getSelectQuery(conn, query)
    
    return {"message": result}


@app.get("/tournaments/{id}")
async def getTournament(id):
    db     = Db()
    conn   = db.connect()

    query      = 'Select id, name, date from tournament where id = ' + id
    tournament = db.getSelectQuery(conn, query)

    conn    = db.connect()
    query   = 'Select id, name, position, idDeck from player where idTournament = ' + id
    players = db.getSelectQuery(conn, query)

    for player in players:
        conn  = db.connect()
        query = 'Select id, name, num, board from deckCards where idDeck = ' + str(player['idDeck'])
        cards = db.getSelectQuery(conn, query)

        player.update({'deck' : cards})

    return {"message": {'tournament' : tournament, 'players' : players }}


@app.get("/tournaments/{id}/stats")
async def getTournamentStats(id):
    # db     = Db()
    # conn   = db.connect()

    # query  = 'Select id, name, date from tournament where id = ' + id
    # result = db.getSelectQuery(conn, query)
    result = 'work in progress'

    return {"message": result}


@app.get("tournaments/{idTournament}/players/{idPlayer}/decks")
async def getPlayerDeck(idTournament, idPlayer):
    # db     = Db()
    # conn   = db.connect()

    # query  = 'Select id, name, date from tournament where id = ' + id
    # result = db.getSelectQuery(conn, query)
    result = 'work in progress'

    return {"message": result}
