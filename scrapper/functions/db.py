import mysql.connector
from mysql.connector import Error
class Db:

    def __init__(self):
        self.hostName        = 'localhost'
        self.portName        = '3308'
        self.databaseName    = 'app-database'
        self.userName        = 'user'
        self.passwordText    = 'password'

    def connection(self):
        connection = None
        try:
            connection = self.connect()

            if connection.is_connected():
                self.connected(connection)

            return connection
                
        except Error as e:
            print("Error while connecting to MySQL %s" %e)
        # finally:
        #     if connection.is_connected():
        #         self.endConnection(connection)

    def connect(self):
        connection = mysql.connector.connect(
            host     = self.hostName,
            port     = self.portName,
            database = self.databaseName,
            user     = self.userName,
            password = self.passwordText
        )

        return connection

    def connected(self, connection):
        try:
            db_Info = connection.get_server_info()
            # print("Connected to MySQL Server version %s" %db_Info)
            cursor = connection.cursor()
            cursor.execute("select database();")
            record = cursor.fetchone()
            # print("You're connected to database: %s" %record)
        except Error as e:
            print("Error while connecting to MySQL %s" %e)

    def endConnection(self, connection):
        try:
            cursor = connection.cursor()
            cursor.close()
            connection.close()
            print("MySQL connection is closed")
        except Error as e:
            print("Error while connecting to MySQL %s" %e)

    def executeQuery(self, connection, query):
        try:
            cursor = connection.cursor()
            cursor.execute(query)
            connection.commit()
            # print(cursor.rowcount, "Record inserted successfully into table")
            cursor.close()
        except Error as e:
            print("Error while connecting to MySQL %s" %e)
    
    def executeInsertQuery(self, connection, query):
        try:
            cursor = connection.cursor()
            cursor.execute(query)
            connection.commit()
            id = cursor.lastrowid
            cursor.close()
            
            return id
        except Error as e:
            print("Error while connecting to MySQL %s" %e)

    def selectQuery(self, connection, query):
        try:
            cursor = connection.cursor()
            cursor.execute(query)
            result = cursor.fetchall()
            final_result = [list(i) for i in result]
            cursor.close()

            return final_result
        except Error as e:
            print("Error while connecting to MySQL %s" %e)
    
    def getOneColumnResultSingleRow(self, result):
        for item in result:
            itemResult = item[0]
            break
        
        return itemResult

    def dropTable(self, connection, tableName):
        try:
            cursor = connection.cursor()
            delete_table_query = "DROP TABLE " + tableName
            cursor.execute(delete_table_query)
        except Error as e:
            print("Error while connecting to MySQL %s" %e)

    def truncateTable(self, connection, tableName):
        try:
            cursor = connection.cursor()
            delete_table_query = "TRUNCATE TABLE " + tableName
            cursor.execute(delete_table_query)
        except Error as e:
            print("Error while connecting to MySQL %s" %e)