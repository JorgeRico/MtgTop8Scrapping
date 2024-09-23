class Card:
    def __init__(self, num, name, idDeck, board):
        self.num    = num
        self.name   = name
        self.board  = board
        self.idDeck = idDeck

    def getNum(self):
        return str(self.num)
    
    def getName(self):
        return str(self.name)
    
    def getBoard(self):
        return str(self.board)
    
    def getIdDeck(self):
        return self.idDeck
    
    def printCard(self):
        return str(self.board) + ': ' + str(self.idDeck) + ' ' + str(self.num) + ' ' + str(self.name)