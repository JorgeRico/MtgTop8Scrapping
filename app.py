from classes.top8 import Top8
from functions.functions import Scrapping
from classes.tournament import Tournament
from classes.league import League

# tournaments
# league and name hardcoded
# ids from www.mtgtop8.com
tournaments = [
    {
        'league' : 1,
        'name'   : 'LCL Ingenio 2024',
        'ids'    : [ 51344, 52277, 53297, 54778, 55496, 56478, 57208, 58206, 59596 ]
    },
    {
        'league' : 2,
        'name'   : 'Lliga Minoria 2024',
        'ids'    :  [ 52033, 52633, 53585, 54411, 55694, 56867, 57385, 58500 ]
    }
]

# scrapping data
def scrapping(id, name, idLeague):
    soup = Scrapping()
    top = Top8()

    # scrapping
    soup = soup.getSoup(soup.getEventUrl(id))
    # Tournament info
    tournament   = Tournament()
    idTournament = tournament.getTournamentData(soup, name, idLeague)
    # top 8 players
    top.setTop8Players(soup, idTournament)
    # decks and cards
    top.setTop8PlayersDecks()

# main function
def main(tournaments):
    for item in tournaments:
        print('   - Scrapping : %s' %(item['name']))
        league = League(item['league'], item['name'])
        league.saveLeague()
        for id in item['ids']:
            print('     * Scrapping tournament id: %s' %(id))
            scrapping(str(id), item['name'], item['league'])


# ---------------------------------
# Start
# ---------------------------------
print(' - Start scrapping !!!')
main(tournaments)
print(' - Finish scrapping !!!')

