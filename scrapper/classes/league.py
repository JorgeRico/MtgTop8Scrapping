from classes.card import Card
from functions.db import Db

class League:
    def __init__(self, id, name):
        self.id   = id
        self.name = name

    def getLeagueId(self):
        return self.id
    
    def getLeagueName(self):
        return self.name

    def saveLeague(self):
        db         = Db()
        connection = db.connection()
        
        query = 'INSERT INTO league (id, name) VALUES ( "%s", "%s" ) ' %(self.id, self.name)
        query += 'ON DUPLICATE KEY UPDATE id="%s", name="%s";' %(self.id, self.name)
        db.executeInsertQuery(connection, query)
