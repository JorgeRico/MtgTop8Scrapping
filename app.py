from classes.top8 import Top8
from functions.functions import Scrapping
from classes.deck import Deck
import sys

soup = Scrapping()
soup = soup.getSoup(soup.getEventUrl('59731'))
			
top = Top8()
top.scrapTopPlayers(soup, "chosen_tr")
top.scrapTopPlayers(soup, "hover_tr")
# top.printTopPlayers()

for player in top.getTopPlayers():
    soup = Scrapping()
    soup = soup.getSoup(player.getPlayerDeckHref())

    deck = Deck()
    deck.getDeck(soup)

    player.setPlayerDeck(deck.getDeckCards())
    # player.printPlayerDeckCards()
    # sys.exit()