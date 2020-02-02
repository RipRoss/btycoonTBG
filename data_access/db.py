import pyodbc
import flask
import hashlib
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
                                   'UID='+self.user+';PWD='+self.password+';', autocommit=True)

    def disconnect(self):
        self.conn.close()

    def proc_confirm_creds(self, username, password):
        self.cursor = self.conn.cursor()
        self.cursor.execute("{CALL confirm_creds (?,?)}", (username, password))
        rows = self.cursor.fetchall()
        return rows

    def proc_create_user(self, username, email, password):
        self.cursor = self.conn.cursor()
        try:
            self.cursor.execute("{CALL create_user (?,?,?)}", (username, email, password))
        except pyodbc.DatabaseError:
            raise
        return True

class User:
    def __init__(self, username, password, email=None):
        self.username = username
        self.password = password
        self.email = email

    def confirm_exists(self):
        """
        uses username and email to ensure that neither of these currently exist, in which case they will have to choose
        something else.
        """
        rows = flask.db.run_proc(f"SELECT 1 FROM users WHERE username='{self.username}' OR email='{self.email}'")
        return rows

    def create_user(self):
        rows = flask.db.proc_create_user(self.username, self.email, str(self.hash_password()))
        return rows

    def confirm_creds(self):
        rows = flask.db.proc_confirm_creds(self.username, str(self.hash_password()))
        return rows

    def hash_password(self):
        pwd = hashlib.md5(self.password.encode()).hexdigest()
        return pwd
