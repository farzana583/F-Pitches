import os

class Config:

  
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:farzana123@localhost/fpitches'
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    SECRET_KEY = os.environ.get('SECRET_KEY')
#  email configurations
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    # simple mde  configurations
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True

class ProdConfig(Config):
    pass


class DevConfig(Config):

    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig,
}