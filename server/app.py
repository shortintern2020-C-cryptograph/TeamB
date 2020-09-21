from flask import Flask, jsonify
from flask_restful import Api
from database import init_db
from apis.genre import GenreListAPI, GenreAPI
from config import Config


def create_app():

    app = Flask(__name__)
    app.config.from_object(Config)

    init_db(app)

    api = Api(app)
    api.add_resource(GenreListAPI, '/communities')
    api.add_resource(GenreAPI, '/communities/<id>')

    return app


app = create_app()
