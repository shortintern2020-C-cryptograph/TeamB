class DevelopmentConfig:

<<<<<<< HEAD
    DEBUG = True

    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{user}:{password}@{host}/{db_name}?charset=utf8'.format(**{
        'user': 'root',
        'password': 'hoge',
        'host': '192.168.33.10:3306',
        'db_name': 'hoge'
    })

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False


Config = DevelopmentConfig
=======
  # SQLAlchemy
  SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{user}:{password}@{host}/{database}?charset=utf8'.format(
    **{
      'user': 'root',
      'password': 'hoge',
      'host': 'db',
      'database': 'hoge',
    })
  SQLALCHEMY_TRACK_MODIFICATIONS = False
  SQLALCHEMY_ECHO = False


Config = DevelopmentConfig
>>>>>>> 2126e8803eaa714c4c3818efc276de8df112fae2
