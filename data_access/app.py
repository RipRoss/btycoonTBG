import flask
import uuid
from data_access import db
from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from login import login
from sessionmanagement import sessions

app_name = 'tbg_data_access'


def create_app():
    return Flask(__name__)


app = create_app()
CORS(app)


# @app.before_request
# @cross_origin()
# def pre_req():
#     req_id = request.headers.get("X-Request-ID", uuid.uuid4())
#     flask.g.request_id = req_id
#
#     flask.db = db.Database()
#     flask.db.connect()
#
#     data = request.get_json()
#
#     authed = login.confirm_user(data["username"], data["password"])
#     if not authed:
#         return jsonify(message="ERROR you fuckin twat")


@app.route('/da/auth_user', methods=['POST'])
@cross_origin()
def auth_user():
    """
    function for authenticating the user
    :return:
    """
    sessions.display_data()
    return jsonify(message="helloworld")
