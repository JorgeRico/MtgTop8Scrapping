from functions.db import Db
from classes.deck import Deck
from functions.functions import Scrapping
class Player:
    def __init__(self, num, playerName, deckName, deckHref):
        self.num        = num
        self.playerName = playerName
        self.deckName   = deckName
        self.deckHref   = deckHref
        self.cards      = None
        self.idPlayer   = None
    
    def getPlayerNum(self):
        return str(self.num)
    
    def getPlayerName(self):
        return str(self.playerName)
    
    def getPlayerDeckName(self):
        return str(self.deckName)
    
    def getPlayerDeckHref(self):
        return str(self.deckHref)
    
    def getPlayerDeck(self):
        return self.cards

    def getIdPlayer(self):
        return self.idPlayer
    
    def setPlayerDeck(self, deck):
        self.cards = deck

    def setIdPlayer(self, idPlayer):
        self.idPlayer = idPlayer

    def setPlayerDeck(self):
        deck   = Deck()
        idDeck = deck.savePlayerDeck(self.getPlayerDeckName(), self.getIdPlayer())
        self.savePlayerIdDeck(idDeck)

        # scrap deck
        soup = Scrapping()
        soup = soup.getSoup(self.getPlayerDeckHref())
        deck.getDeck(idDeck, soup)

    def savePlayer(self, idTournament):
        db          = Db()
        connection  = db.connection()
        query       = 'INSERT INTO player (name, position, idTournament) VALUES ( "%s", "%s", "%s" );' %(self.getPlayerName(), self.getPlayerNum(), idTournament)
        self.setIdPlayer(db.executeInsertQuery(connection, query))
    
    def savePlayerIdDeck(self, idDeck):
        db          = Db()
        connection  = db.connection()
        updateQuery = "UPDATE player SET idDeck = '%s' WHERE id = '%s'" %(idDeck, self.idPlayer)
        db.executeQuery(connection, updateQuery)

    def printPlayerDeckCards(self):
        for item in self.cards:
            print(item.printCard())
