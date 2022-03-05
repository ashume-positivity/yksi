import pytest
from flask import Flask


def App():
    app = Flask(__name__)
    @app.route('/')
    def getGameState():
        return {'Hello': 'World'}
    return app


@pytest.fixture()
def app():
    app = App()
    app.config.update({
        "TESTING": True,
    })

    yield app


@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def runner(app):
    return app.test_cli_runner()
