from flask_sqlalchemy import SQLAlchemy
<<<<<<< HEAD
=======

>>>>>>> 2126e8803eaa714c4c3818efc276de8df112fae2
from flask_migrate import Migrate


db = SQLAlchemy()


def init_db(app):
  db.init_app(app)
  Migrate(app, db)
