from functions.functions import Scrapping
from classes.player import Player

class Top8:
    def __init__(self):
        self.topPlayers = []
    
    def setTopPlayer(self, deckName, playerName, deckHref):
        scrapping = Scrapping()
        if deckName != '' and playerName != '' and deckHref != '':
            num = len(self.topPlayers)
            player = Player(num+1, playerName, deckName, scrapping.getPlayerDeckUrl(deckHref))
            self.topPlayers.append(player)
            
            return True
        
        return False

    def scrapTopPlayers(self, soup, className):
        for set in soup.findAll('div', attrs={"class": className}):
            num = 0

            for link in set.find_all('a'):

                if link.text != '':
                    if num == 0:
                        deckName = link.text
                        deckHref = link.get('href')
                    if num == 1:
                        playerName = link.text
                    num+=1
            
            if self.setTopPlayer(deckName, playerName, deckHref) == True:
                deckName   = ''
                playerName = ''

    def getTopPlayers(self):
        return self.topPlayers
    
    def printTopPlayers(self):
        for item in self.topPlayers:
            print(' - ' + str(item.getPlayerNum()) + ' ||| ' + item.getPlayerName() + ' ||| ' + item.getPlayerDeckName() + ' ||| ' + item.getPlayerDeckHref())