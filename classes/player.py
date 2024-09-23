class Player:
    def __init__(self, num, playerName, deckName, deckHref):
        self.num        = num
        self.playerName = playerName
        self.deckName   = deckName
        self.deckHref   = deckHref
        self.cards      = None
    
    def getPlayerNum(self):
        return self.num
    
    def getPlayerName(self):
        return self.playerName
    
    def getPlayerDeckName(self):
        return self.deckName
    
    def getPlayerDeckHref(self):
        return self.deckHref
    
    def getPlayerDeck(self):
        return self.cards
    
    def setPlayerDeck(self, deck):
        self.cards = deck

    def printPlayerDeckCards(self):
        for item in self.cards:
            print(item.printCard())