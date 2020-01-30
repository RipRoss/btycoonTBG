import flask
import uuid
from data_access import db
from flask import Flask, jsonify, request, Response, jsonify
from sessionmanagement import wsgi
from login import login

app_name = 'tbg_data_access'


def create_app():
    return Flask(__name__)


app = create_app()


@app.before_request
def request_id():
    req_id = request.headers.get("X-Request-ID", uuid.uuid4())
    flask.g.request_id = req_id


@app.before_request
def init_db():
    flask.db = db.Database()
    flask.db.connect()


@app.route('/da/auth_user', methods=['POST'])
def auth_user():
    """
    function for authenticating the user
    :return:
    """
    creds = request.get_json()

    authed = login.confirm_user(creds["username"], creds["password"])

    if not authed:
        return Response("{'authed': False}", status=401, mimetype='application/json')
    return jsonify(authed)
