from flask import Flask, request

_app_name = "register_user"


def create_app():
    return Flask(__name__)


app = create_app()


@app.route('/api/register', methods=['POST'])
def register_user():
    creds = request.get_json()

