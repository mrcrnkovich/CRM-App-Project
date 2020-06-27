# Configuration File
import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = "Any_Secret_Key"

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    SQLALCHEMY_DATABASE_URI = (
        "postgresql://postgres:secretPassword@crm-compose-db:5432/crmDatabase"
    )


class DevelopmentConfig(Config):
    """
    Development configurations
    """

    DEBUG = True
    RELOAD = True
    SQLALCHEMY_ECHO = True


class ProductionConfig(Config):
    """
    Production configurations
    """

    DEBUG = False


app_config = {"development": DevelopmentConfig, "production": ProductionConfig}
