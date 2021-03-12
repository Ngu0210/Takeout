import os

class Config(object):
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = '4124'

class DevelopmentConfig(Config):
    DEBUG = True
    
    @property
    def SQLALCHEMY_DATABASE_URI(self):
        value = os.getenv("DB_URI_TEST")

        if not value:
            raise ValueError("DB_URI is not set!")

        return value

class ProductionConfig(Config):
    @property
    def JWT_SECRET_KEY(self):
        value = os.getenv("JWE_SECRET_KEY")

        if not value:
            raise ValueError("JWT_SECRET_KET is not set")

        return value

    @property
    def SQLALCHEMY_DATABASE_URI(self):
        value = os.getenv("DB_URI")

        if not value:
            raise ValueError("DB_URI is not set!")

        return value

class TestingConfig(Config):
    TESTING = True

environment = os.getenv("FLASK_ENV")

if environment == "production":
    app_config = ProductionConfig()
elif environment == "testing":
    app_config = TestingConfig()
else:
    app_config = DevelopmentConfig()
