import flask
from flask import Flask

def create_app():
    app = Flask(__name__)
    played_ = {'lastPlayed': '0'}

    @app.route('/')
    def getGameState():
        return played_

    @app.route('/', methods=['PUT'])
    def putGameState():
        nonlocal played_
        played_ = flask.request.json
        return played_

    return app
