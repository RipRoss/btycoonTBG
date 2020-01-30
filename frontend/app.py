from flask import Flask, render_template

app_name = "btycoon_fe"


def create_app():
    return Flask(__name__)


app = create_app()


@app.route('/home', methods=['GET'])
def display_home():
    return render_template('home.html')