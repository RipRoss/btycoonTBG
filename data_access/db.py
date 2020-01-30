import pyodbc
from data_access import config


class Database:
    def __init__(self):
        self.host = config.db_config["host"]
        self.database = config.db_config["database"]
        self.user = config.db_config["user"]
        self.password = config.db_config["password"]
        self.conn = None
        self.cursor = None

    def connect(self):
        self.conn = pyodbc.connect('DRIVER=ODBC Driver 17 for SQL Server;SERVER='+self.host+';DATABASE='+self.database+';'
                                   'UID='+self.user+';PWD='+self.password+';')

    def disconnect(self):
        self.conn.close()

    def run_query(self, query):
        self.cursor = self.conn.cursor()
        self.cursor.execute(query)
        rows = self.cursor.fetchall()
        return rows
