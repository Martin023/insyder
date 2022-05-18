import os
class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://martin023:0000@localhost/insyder'
    SECRET_KEY = 'werkzeug'
    QUOTES_API_BASE_URL = 'http://quotes.stormconsultancy.co.uk/random.json'
    UPLOADED_PHOTOS_DEST ='app/static/photos'

    
class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://martin023:0000@localhost/insyder'
    if SQLALCHEMY_DATABASE_URI.startswith("postgres://"):
        SQLALCHEMY_DATABASE_URI =SQLALCHEMY_DATABASE_URI.replace("postgres://","postgresql://",)
    

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://martin023:0000@localhost/insyder'
    
    DEBUG = True
    
class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://martin023:0000@localhost/blog_test'

    
    
    
config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig
}

