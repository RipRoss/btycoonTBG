from flask import Flask, Response, request
import flask
from sessionmanagement import wsgi

app = Flask(__name__)


@app.route('/user/confirm', methods=['POST'])
def confirm_user():
    creds = request.get_json()
    #check if the user has a session in REDIS first.
    rows = flask.db.run_query(f"SELECT userid FROM users WHERE username='{creds['username']}' AND "
                              f"password='{creds['password']}'")

    if not rows:
        #not authed
        return Response("", status=401, mimetype='application/json')

    session = wsgi.confirm_session(rows[0][0])
    return session
