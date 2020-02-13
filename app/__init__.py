from flask import Flask
from .views.index import home
from .views.messages import messages
import tweepy


def create_app():
    app = Flask(
        __name__,
        instance_relative_config=False,
        static_folder='static',
    )

    app.config.from_object('config.DevelopmentConfig')
    app.register_blueprint(home)
    app.register_blueprint(messages)
    return app