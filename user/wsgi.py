from flask import Flask, Response, request, jsonify
import flask
from .data_access import db
from .data_access import wsgi
import pyodbc


app = Flask(__name__)


@app.before_request
def init_db():
    try:
        flask.db = db.Database()
        flask.db.connect()
    except pyodbc.DatabaseError as e:
        raise e


@app.before_request
def init_user():
    creds = request.get_json()

    flask.user = db.User(creds["username"], creds["password"], creds["email"])


@app.route('/user/confirm', methods=['POST'])
def confirm_user():
    authentication = wsgi.login_user(flask.user.get_username())
    if authentication is None:
        return Response("", status=401)
    return authentication


@app.route('/user/create', methods=['POST'])
def create_user():
    wsgi.create_user()
    return jsonify(created=True)


@app.teardown_request
def disc_db(exc):
    flask.db.disconnect()
