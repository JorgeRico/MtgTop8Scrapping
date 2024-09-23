class Card:
    def __init__(self, num, name, id):
        self.num  = num
        self.name = name
        self.id   = id

    def printCard(self):
        return self.id + ': ' + self.num + ' ' + self.name