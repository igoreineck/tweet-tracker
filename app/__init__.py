from flask import Flask
from .views.index import home
from .views.hashtags import hashtag_save, hashtag_retrieve
from .views.messages import message_retrieve
import tweepy

_ROUTES = [
    home,
    hashtag_save,
    hashtag_retrieve,
    message_retrieve,
]

def create_app():
    app = Flask(
        __name__,
        instance_relative_config=False,
        static_folder='static',
    )
    app_settings(app)
    register_blueprints(app)
    return app

def app_settings(app):
    app.config.from_object('config.DevelopmentConfig')
    return app

def register_blueprints(app):
    for route in _ROUTES:
        app.register_blueprint(route)
    return app