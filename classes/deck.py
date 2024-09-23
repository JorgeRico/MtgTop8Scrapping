from classes.card import Card

class Deck:
    def __init__(self):
        self.cards = []

    def getDeck(self, soup):
        for cards in soup.findAll('div', attrs={"class": 'deck_line hover_tr'}):
            id = cards.get('id')[:2]

            if cards.text[1] == ' ':
                num  = cards.text[0]
                name = cards.text[2:]
            if cards.text[2] == ' ':
                num  = cards.text[:2]
                name = cards.text[3:]
            
            card = Card(num, name, id)
            self.cards.append(card)
    
    def getDeckCards(self):
        return self.cards
    
    def printDeckCards(self):
        for item in self.cards:
            print(item.textCard)