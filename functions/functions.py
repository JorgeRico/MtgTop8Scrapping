import urllib
import urllib.request
from bs4 import BeautifulSoup

class Scrapping:
    def __init__(self):
        self.baseurl = 'https://www.mtgtop8.com/event'

    def getEventUrl(self, url):
        return self.baseurl + '?e=' + url + '&f=LE'

    # get soup
    def getSoup(self, url):
        page = urllib.request.urlopen(url)
        soup = BeautifulSoup(page, 'html.parser')

        return soup
    
    def getPlayerDeckUrl(self, url):
        return self.baseurl + url
