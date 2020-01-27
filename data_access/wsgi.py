import pyodbc
from flask import Flask, jsonify, request, make_response

app_name = 'tbg_data_access'


def create_app():
    return Flask(__name__)


app = create_app()


# @app.before_request
# def request_id():
#     print(uuid.uuid4())
#     headers = request.headers
#
#     if getattr(headers, "X-Request-ID"):
#         flask.g.request_id = request.headers.get('X-Request-ID')
#     else:
#         flask.g.request_id = uuid.uuid4()


@app.route('/da/auth_user', methods=['POST'])
def auth_user():
    """
    function for authenticating the user
    :return:
    """
    creds = request.get_json()

    user = creds["username"]
    password = creds["password"]

    with pyodbc.connect('DRIVER=ODBC Driver 17 for SQL Server;SERVER=localhost;DATABASE=btycoon;'
                        'UID=sa;PWD=Caiden8839;') as conn:
        csr = conn.cursor()
        csr.execute(f"SELECT * FROM users where username='{user}' and password='{password}'")
        rows = csr.fetchall()

    if len(rows) == 1:
        resp = make_response(jsonify(authenticated=True))
        resp.set_cookie('username', str(rows[0][0]).rjust(8, "0"))
        return resp

    return jsonify(authenticated=False)
