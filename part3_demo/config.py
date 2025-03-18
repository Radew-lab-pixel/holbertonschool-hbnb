import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'default_secret_key')
    DEBUG = False

class DevelopmentConfig(Config):
    # SQLALCHEMY_DATABASE_URI = 'mysql://username:password@localhost/hbnb_evo_2_db'
    DEBUG = True

config = {
    'development': DevelopmentConfig,
    'default': DevelopmentConfig
}