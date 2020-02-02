import flask
from flask import Flask, request, Response
import uuid
from sessionmanagement import Session, RedisInit


app = Flask(__name__)


@app.route('/api/auth', methods=['POST'])
def confirm_user():
    json_data = request.get_json()

    if _confirm_payload(json_data) is None:
        r = Session.Session(username=json_data["username"])
        sess = r.create_session()
        if not sess:
            return Response("", status=500, mimetype='application/json')
        return Response("", status=200, mimetype='application/json')

    if not _confirm_payload(json_data):
        return Response("", status=400, mimetype='application/json')

    r = Session.Session(session_key=json_data['session_key'], username=json_data['username'])

    if not r.confirm_session():
        return Response("", status=401, mimetype='application/json')
    return Response("", status=200, mimetype='application/json')


@app.route('/api/clear_db', methods=['GET'])
def clear_db():
    r = RedisInit.RedisInit()
    r.clear_db()


def _confirm_payload(payload):
    if not payload or 'session_key' not in payload and 'username' not in payload:
        return False
    elif 'session_key' not in payload and 'username' in payload:
        return None
    return True


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
