import flask
import pyodbc
from flask import Flask, jsonify, request
import uuid

app_name = 'tbg_data_access'


def create_app():
    return Flask(__name__)


app = create_app()


@app.before_request
def request_id():
    print(uuid.uuid4())
    headers = request.headers

    if getattr(headers, "X-Request-ID"):
        flask.g.request_id = request.headers.get('X-Request-ID')
    else:
        flask.g.request_id = uuid.uuid4()


@app.route('/da/auth_user', methods=['POST'])
def auth_user():
    """
    function for authenticating the user
    :return:
    """
    creds = request.get_json()

    user = creds["username"]
    password = creds["password"]

    print(flask.g.request_id)

    with pyodbc.connect('DRIVER={driver};' 'SERVER={server};' 'DATABASE={database};'
                        'UID={uid};' 'PWD={pwd};'.format(driver="ODBC Driver 17 for SQL Server",
                                                         server="localhost", database="textbasedtycoon",
                                                         uid="sa", pwd="Caiden8839")) as conn:
        csr = conn.cursor()
        csr.execute(f"SELECT * FROM users where username='{user}' and password='{password}'")
        rows = csr.fetchall()

        if rows:
            return jsonify(authenticated=True)
