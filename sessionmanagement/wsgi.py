import flask
from flask import Flask, request
import uuid

app = Flask(__name__)


def generate_auth_token():
    return uuid.uuid4()


def confirm_session(userid):
    rows = flask.db.run_query("SELECT users.username, users.userid, users.email, sessions.session_id FROM users, "
                              f"sessions WHERE users.userid = '{userid}' AND users.userid = sessions.userid")

    _session = {
        "username": "",
        "userid": "",
        "email": "",
        "auth_token": ""
    }

    for row in rows:
        _session["username"] = row[0]
        _session["userid"] = row[1]
        _session["email"] = row[2]
        _session["auth_token"] = row[3]
        return _session
