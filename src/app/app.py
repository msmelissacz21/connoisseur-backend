from flask import Flask
from app.ping.controller import ping
from app.recipies.controller import recipes
from app.users.controller import users

flask_app = Flask(__name__)

def create_app():
    flask_app.register_blueprint(ping)
    flask_app.register_blueprint(recipes)
    flask_app.register_blueprint(users)
    return flask_app