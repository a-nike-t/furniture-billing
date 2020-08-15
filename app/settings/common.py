import logging

APP_NAME = 'furniture-billing'
LOGGER_NAME = APP_NAME
DEBUG = False
TESTING = False
# to fix the issue of flask_restful
# using flask error handlers instead of flask_restful's
PROPAGATE_EXCEPTIONS = True
LOGGING_LEVEL = logging.INFO
SQLALCHEMY_TRACK_MODIFICATIONS = True
INGEST_TO_DB = True
