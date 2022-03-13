import flask
from flask import Flask, Blueprint


def create_app():
    app = Flask(__name__)

    controller = Controller()

    app.register_blueprint(controller.blueprint())

    return app


class Controller:

    def __init__(self):
        self.played_ = {'lastPlayed': '0'}

    def getGameState(self):
        return self.played_

    def putGameState(self):
        self.played_ = flask.request.json
        return self.played_

    def blueprint(self):
        blueprint = Blueprint('', __name__)
        blueprint.route('/')(self.getGameState)
        blueprint.route('/', methods=['PUT'])(self.putGameState)
        return blueprint
