from fastapi import FastAPI, HTTPException, Path
from db.db import Db
from typing import Any
from models.league import League
from models.tournament import Tournament, TournamentData
from models.player import Player, PlayerData
from models.card import Card, TopCard, MAINDECK_CARD, SIDEBOARD_CARD
from models.deck import Deck
from errors.errors import notFound
from codes.codes import HTTP_200, HTTP_404

app = FastAPI(exception_handlers={
    404: notFound
})

@app.get("/health", status_code=HTTP_200, description="Health endpoint")
async def index():
    return {"message": "It works !!!!"}

# ---------------------------------------------
# League endpoints
# ---------------------------------------------
@app.get("/leagues/{id}", response_model=League, status_code=HTTP_200, description="League info")
async def getLeagueData(id: int = Path(gt = 0, title="Id League", description="League resource identifier")) -> Any:
    db     = Db()
    conn   = db.connect()

    query  = 'SELECT id, name FROM league WHERE id = ' + str(id)
    result = db.getSelectSingleResultQuery(conn, query)

    if result is None or id is None:
        raise HTTPException(status_code=HTTP_404, detail="League not found")

    return result

@app.get("/leagues/{id}/tournaments", response_model=list[Tournament], status_code=HTTP_200, description="League Tournaments list")
async def getLeagueTournamentsData(id: int = Path(gt = 0, title="Id League", description="League resource identifier"), skip: int = 0, limit: int = 10) -> Any:
    db     = Db()
    conn   = db.connect()

    query  = 'SELECT id, name, date FROM tournament WHERE idLeague = ' + str(id) + ' LIMIT ' + str(skip) + ', ' + str(limit)
    result = db.getSelectListResultQuery(conn, query)
    
    if len(result) == 0:
        raise HTTPException(status_code=HTTP_404, detail="No items found")

    return result

# ---------------------------------------------
# Tournament endpoints
# ---------------------------------------------
@app.get("/tournaments/{id}", response_model=Tournament, status_code=HTTP_200, description="Tournament info")
async def getTournament(id: int = Path(gt = 0, title="Id Tournament", description="Tournament resource identifier")) -> Any:
    db     = Db()
    conn   = db.connect()

    query  = 'SELECT id, name, date FROM tournament WHERE id = ' + str(id)
    result = db.getSelectSingleResultQuery(conn, query)
    
    if result == None:
        raise HTTPException(status_code=HTTP_404, detail="Item not found")

    return result

@app.get("/tournaments/{id}/players", response_model=list[Player], status_code=HTTP_200, description="Tournament players list")
async def getTournamentPlayers(id: int = Path(gt = 0, title="Id Tournament", description="Tournament resource identifier")) -> Any:
    db     = Db()
    conn   = db.connect()

    query  = 'SELECT id, name, position, idDeck FROM player WHERE idTournament = ' + str(id)
    result = db.getSelectListResultQuery(conn, query)

    if len(result) == 0:
        raise HTTPException(status_code=HTTP_404, detail="No items found")

    return result

@app.get("/tournaments/{id}/decks", response_model=list[Deck], status_code=HTTP_200, description="Tournament decks")
async def getTournamentDecks(id: int = Path(gt = 0, title="Id Tournament", description="Tournament resource identifier")) -> Any:
    db    = Db()
    conn  = db.connect()

    query =  "SELECT deck.id, deck.name FROM player "
    query += "INNER JOIN tournament on tournament.id = player.idTournament "
    query += "INNER JOIN deck on deck.id = player.idDeck "
    query += "WHERE tournament.id = " + str(id) + " "

    result = db.getSelectListResultQuery(conn, query)

    if len(result) == 0:
        raise HTTPException(status_code=HTTP_404, detail="No items found")

    return result

@app.get("/tournaments/{id}/data", response_model=TournamentData, status_code=HTTP_200, description="Tournament info, players and decks")
async def getTournamentData(id: int = Path(gt = 0, title="Id Tournament", description="Tournament resource identifier")) -> Any:
    tournament = await getTournament(str(id))
    players    = await getTournamentPlayers(str(id))

    for player in players:
        cards = await getDeckCards(player['idDeck'])
        player.update({'deck' : cards})

    if tournament == None:
        raise HTTPException(status_code=HTTP_404, detail="Item not found")
    if len(players) == 0:
        raise HTTPException(status_code=HTTP_404, detail="Item with no players")

    return TournamentData(tournament=tournament, players=players)


# ---------------------------------------------
# Player endpoints
# ---------------------------------------------
@app.get("/players/{id}", response_model=Player, status_code=HTTP_200, description="Player info")
async def getPlayer(id: int = Path(gt = 0, title="Id Player", description="Player resource identifier")) -> Any:
    db     = Db()
    conn   = db.connect()

    query  = 'SELECT id, name, position, idDeck FROM player WHERE id = ' + str(id)
    result = db.getSelectSingleResultQuery(conn, query)

    if result == None:
        raise HTTPException(status_code=HTTP_404, detail="Item not found")

    return result

@app.get("/players/{id}/data", response_model=PlayerData, status_code=HTTP_200, description="Player info and deck list")
async def getPlayerDeckData(id: int = Path(gt = 0, title="Id Player", description="Player resource identifier")) -> Any:
    db     = Db()
    conn   = db.connect()

    query  = 'SELECT id, name, position, idDeck FROM player WHERE id = ' + str(id)
    result = db.getSelectSingleResultQuery(conn, query)

    cards = await getDeckCards(result['idDeck'])
    result.update({'deck' : cards})
    
    if result == None:
        raise HTTPException(status_code=HTTP_404, detail="Item not found")
    if len(cards) == None:
        raise HTTPException(status_code=HTTP_404, detail="Item with no cards")

    return result

@app.get("/players/{id}/decks", response_model=Deck, status_code=HTTP_200, description="Player deck list")
async def getPlayerDeck(id: int = Path(gt = 0, title="Id Player", description="Player resource identifier")) -> Any:
    db     = Db()
    conn   = db.connect()

    query  = 'SELECT id, name FROM deck WHERE idPlayer = ' + str(id)
    result = db.getSelectSingleResultQuery(conn, query)
    
    if result == None:
        raise HTTPException(status_code=HTTP_404, detail="Item not found")

    return result


# ---------------------------------------------
# Deck endpoints
# ---------------------------------------------
@app.get("/decks/{id}/cards", response_model=list[Card], status_code=HTTP_200, description="Deck cards list")
async def getDeckCards(id: int = Path(gt = 0, title="Id Deck", description="Deck resource identifier")) -> Any:
    db     = Db()
    conn   = db.connect()

    query  = 'SELECT id, name, num, board FROM cards WHERE idDeck = ' + str(id)
    result = db.getSelectListResultQuery(conn, query)

    if len(result) == 0:
        raise HTTPException(status_code=HTTP_404, detail="No items found")

    return result


# ---------------------------------------------
# League Stats endpoints
# ---------------------------------------------
@app.get("/stats/leagues/{id}/cards", response_model=list[TopCard], status_code=HTTP_200, description="Top 10 league cards list")
async def getTop10LeagueCards(id: int = Path(gt = 0, title="Id League", description="League resource identifier")):
    db     = Db()
    conn   = db.connect()

    query = "SELECT SUM(cards.num) as num, cards.name FROM cards "
    query +="INNER JOIN player ON player.idDeck = cards.idDeck "
    query +="INNER JOIN tournament ON tournament.id = player.idTournament "
    query +="WHERE tournament.idLeague = " + str(id) + " "
    query +="GROUP BY cards.name "
    query +="ORDER BY num desc "
    query +="LIMIT 20;"

    result = db.getSelectListResultQuery(conn, query)

    if len(result) == 0:
        raise HTTPException(status_code=HTTP_404, detail="No items found")

    return result

@app.get("/stats/leagues/{id}/main/cards", response_model=list[TopCard], status_code=HTTP_200, description="Top 10 Maindeck League cards list")
async def getTop10LeagueMdCards(id: int = Path(gt = 0, title="Id League", description="League resource identifier")):
    db     = Db()
    conn   = db.connect()

    query = "SELECT SUM(cards.num) as num, cards.name FROM cards "
    query +="INNER JOIN player ON player.idDeck = cards.idDeck "
    query +="INNER JOIN tournament ON tournament.id = player.idTournament "
    query +="WHERE tournament.idLeague = " + str(id) + " and cards.board = '" + MAINDECK_CARD + "' "
    query +="GROUP BY cards.name "
    query +="ORDER BY num desc "
    query +="LIMIT 20;"

    result = db.getSelectListResultQuery(conn, query)

    if len(result) == 0:
        raise HTTPException(status_code=HTTP_404, detail="No items found")

    return result

@app.get("/stats/leagues/{id}/side/cards", response_model=list[TopCard], status_code=HTTP_200, description="Top 10 Sideboard League cards list")
async def getTop10LeagueSbCards(id: int = Path(gt = 0, title="Id League", description="League resource identifier")):
    db     = Db()
    conn   = db.connect()

    query = "SELECT SUM(cards.num) as num, cards.name FROM cards "
    query +="INNER JOIN player ON player.idDeck = cards.idDeck "
    query +="INNER JOIN tournament ON tournament.id = player.idTournament "
    query +="WHERE tournament.idLeague = " + str(id) + " AND cards.board = '" + SIDEBOARD_CARD + "' "
    query +="GROUP BY cards.name "
    query +="ORDER BY num desc "
    query +="LIMIT 20;"

    result = db.getSelectListResultQuery(conn, query)

    if len(result) == 0:
        raise HTTPException(status_code=HTTP_404, detail="No items found")

    return result

@app.get("/stats/leagues/{id}/players", response_model=list[TopCard], status_code=HTTP_200, description="Top 10 Players list")
async def getTop10Players(id: int = Path(gt = 0, title="Id League", description="League resource identifier")):
    db     = Db()
    conn   = db.connect()

    query = "SELECT COUNT(player.name) as num, player.name FROM player "
    query +="INNER JOIN tournament ON tournament.id = player.idTournament "
    query +="WHERE tournament.idLeague = " + str(id) + " "
    query +="GROUP BY player.name "
    query +="ORDER BY num desc "
    # query +="LIMIT 10;"

    result = db.getSelectListResultQuery(conn, query)

    if len(result) == 0:
        raise HTTPException(status_code=HTTP_404, detail="No items found")

    return result

# ---------------------------------------------
# Tournament Stats endpoints
# ---------------------------------------------
@app.get("/stats/tournaments/{id}/cards", response_model=list[TopCard], status_code=HTTP_200, description="Top 10 tournament cards list")
async def getTop10TournamentCards(id: int = Path(gt = 0, title="Id Tournament", description="Tournament resource identifier")):
    db     = Db()
    conn   = db.connect()

    query = "SELECT SUM(cards.num) as num, cards.name FROM cards "
    query +="INNER JOIN player ON player.idDeck = cards.idDeck "
    query +="INNER JOIN tournament ON tournament.id = player.idTournament "
    query +="WHERE tournament.id = " + str(id) + " "
    query +="GROUP BY cards.name "
    query +="ORDER BY num desc "
    query +="LIMIT 10;"

    result = db.getSelectListResultQuery(conn, query)

    if len(result) == 0:
        raise HTTPException(status_code=HTTP_404, detail="No items found")

    return result

@app.get("/stats/tournaments/{id}/main/cards", response_model=list[TopCard], status_code=HTTP_200, description="Top 10 Maindeck tournament cards list")
async def getTop10TournamentMdCards(id: int = Path(gt = 0, title="Id Tournament", description="Tournament resource identifier")):
    db     = Db()
    conn   = db.connect()

    query = "SELECT SUM(cards.num) as num, cards.name FROM cards "
    query +="INNER JOIN player ON player.idDeck = cards.idDeck "
    query +="INNER JOIN tournament ON tournament.id = player.idTournament "
    query +="WHERE tournament.id = " + str(id) + " and cards.board = '" + MAINDECK_CARD + "' "
    query +="GROUP BY cards.name "
    query +="ORDER BY num desc "
    query +="LIMIT 10;"

    result = db.getSelectListResultQuery(conn, query)

    if len(result) == 0:
        raise HTTPException(status_code=HTTP_404, detail="No items found")

    return result

@app.get("/stats/tournaments/{id}/side/cards", response_model=list[TopCard], status_code=HTTP_200, description="Top 10 Sideboard tournament cards list")
async def getTop10TournamentSbCards(id: int = Path(gt = 0, title="Id Tournament", description="Tournament resource identifier")):
    db     = Db()
    conn   = db.connect()

    query = "SELECT SUM(cards.num) as num, cards.name FROM cards "
    query +="INNER JOIN player ON player.idDeck = cards.idDeck "
    query +="INNER JOIN tournament ON tournament.id = player.idTournament "
    query +="WHERE tournament.id = " + str(id) + " AND cards.board = '" + SIDEBOARD_CARD + "' "
    query +="GROUP BY cards.name "
    query +="ORDER BY num desc "
    query +="LIMIT 10;"

    result = db.getSelectListResultQuery(conn, query)

    if len(result) == 0:
        raise HTTPException(status_code=HTTP_404, detail="No items found")

    return result