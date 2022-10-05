from flask import Flask
from app.ping.controller import ping

flask_app = Flask(__name__)

def create_app():
    flask_app.register_blueprint(ping)

    return flask_app