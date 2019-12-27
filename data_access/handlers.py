from flask import jsonify
from flask_cors import cross_origin

from data_access import app


@app.route('/', methods=['GET'])
@cross_origin()
def default_route():
    return jsonify(isittrue=app.config['DEFAULT']['default'])

