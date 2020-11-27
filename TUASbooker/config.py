class Config:
    DEBUG = True

    SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://db:db@localhost/diy"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    SECRET_KEY = "super-duper-secret-key"
    JWT_ERROR_MESSAGE_KEY = "message"
    JWT_BLACKLIST_ENABLED = True
    JWT_BLACKLIST_TOKEN_CHECKS = ['access', 'refresh']