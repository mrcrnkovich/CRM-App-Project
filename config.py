import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
	SECRET_KEY	= 'Any_Secret_Key'

	SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
		'sqlite:///' + os.path.join(basedir, 'crm.db')
	SQLALCHEMY_TRACK_MODIFICATIONS = False
	
	MAIL_SERVER = 'smtp.gmail.com'
	MAIL_PORT = 465
	MAIL_USERNAME = 'mrcrnkovich@gmail.com'
	MAIL_PASSWORD = 'tllraxbcvqhinalf'
	MAIL_USE_TLS = False
	MAIL_USE_SSL = True


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

app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}