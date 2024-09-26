from classes.card import Card
from functions.db import Db
class Deck:
    def __init__(self):
        self.cards = []

    def getDeckCards(self):
        return self.cards

    def getDeck(self, idDeck, soup):
        for cards in soup.findAll('div', attrs={"class": 'deck_line hover_tr'}):
            board = cards.get('id')[:2]

            if cards.text[1] == ' ':
                num  = cards.text[0]
                name = cards.text[2:]
            if cards.text[2] == ' ':
                num  = cards.text[:2]
                name = cards.text[3:]
            
            card = Card(num, name, idDeck, board)
            self.cards.append(card)
            self.saveDeckCard(card)

    def savePlayerDeck(self, name, idPlayer):
        db         = Db()
        connection = db.connection()
        query      = 'INSERT INTO deck (name, idPlayer) VALUES ( "%s", "%s" );' %(name, idPlayer)
        return db.executeInsertQuery(connection, query)

    def saveDeckCard(self, card):
        db         = Db()
        connection = db.connection()
        query      = 'INSERT INTO cards (name, num, idDeck, board) VALUES ( "%s", "%s", "%s", "%s" );' %(card.getName().strip(), card.getNum(), card.getIdDeck(), card.getBoard())
        db.executeInsertQuery(connection, query)
    
    def printDeckCards(self):
        for item in self.cards:
            print(item.textCard)