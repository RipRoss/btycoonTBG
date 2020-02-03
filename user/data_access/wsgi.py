import flask
from flask import Flask, request, Response, jsonify
from user.data_access import db
import requests
import json

_app_name = "data_access"


def create_app():
    return Flask(__name__)


app = create_app()


def create_user():
    flask.user.create_user()

    return Response("", status=200)


def login_user(username):
    rows = flask.user.confirm_creds()

    if rows:
        # authenticated. Create session and return that session in either header, or json
        data = _create_session(username)
        return jsonify(session_key=data["session_key"], username=data["username"])
    return None


def _create_session(username):
    payload = {
        "username": username
    }

    try:
        resp = requests.post("http://localhost:5001/sm/auth", json=payload)
        resp.raise_for_status()
        json_data = json.loads(resp.text)
        print(json_data)
        return json_data
    except requests.exceptions.RequestException as e:
        raise e
