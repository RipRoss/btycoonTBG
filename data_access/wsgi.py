import flask
from flask import Flask, request, Response
from data_access import db


_app_name = "data_access"


def create_app():
    return Flask(__name__)


app = create_app()


@app.before_request
def init_db():
    flask.db = db.Database()
    flask.db.connect()


@app.route('/da/create_user', methods=['POST'])
def create_user():
    creds = request.get_json()

    user = db.User(creds["username"], creds["password"], creds["email"])

    user.create_user()

    return Response("", status=200)
