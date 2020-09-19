from flask import Flask, jsonify
<<<<<<< HEAD
from flask_restful import Api
from .database import init_db
from .apis.hoge import HogeListAPI, HogeAPI
from .config import Config


def create_app():

    app = Flask(__name__)
    app.config.from_object(Config)

    init_db(app)

    api = Api(app)
    api.add_resource(HogeListAPI, '/hoges')
    api.add_resource(HogeAPI, '/hoges/<id>')

    return app


app = create_app()
=======

from flask_restful import Api

from database import init_db

from apis.hoge import HogeListAPI, HogeAPI
from apis.genre import GenreAPI

def create_app():

  app = Flask(__name__)
  app.config.from_object('config.Config')

  init_db(app)

  api = Api(app)
  api.add_resource(HogeListAPI, '/hoges')
  api.add_resource(HogeAPI, '/hoges/<id>')
  api.add_resource(GenreAPI, '/community/<id>')

  return app


app = create_app()
>>>>>>> 2126e8803eaa714c4c3818efc276de8df112fae2
