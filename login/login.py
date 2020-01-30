from flask import Flask, Response, jsonify
import flask
from sessionmanagement import wsgi

app = Flask(__name__)


def confirm_user(username, password):
    #check if the user has a session in REDIS first.
    rows = flask.db.run_query(f"SELECT userid FROM users WHERE username='{username}' AND password='{password}'")

    if not rows:
        #not authed
        return Response("", status=401, mimetype='application/json')

    session = wsgi.confirm_session(rows[0][0])
    return session