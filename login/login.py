from flask import Flask
import flask
from data_access import db

app = Flask(__name__)


def confirm_user(username, password):
    rows = flask.db.run_query(f"SELECT * FROM users WHERE username={username} AND password={password}")
    print(rows)