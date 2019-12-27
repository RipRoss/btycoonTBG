from flask import Flask

app = Flask(__name__)

app.config.from_json('settings.json')

from data_access import handlers
