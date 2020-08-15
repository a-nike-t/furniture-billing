from .common import *  # NOQA

HOST_URL = '127.0.0.1'
HOST_PORT = 5002
DEBUG = True
TESTING = False
SENTRY_DSN = ""

AUTH_VERSION = 1

POSTGRES = {
    "user": "ingestion_app_embibe",
    "password": "ingestion_app1",
    "db": "book_ingestion",
    "host": "127.0.0.1",
    "port": "5432",
}

SQLALCHEMY_DATABASE_URI = (
    'postgresql://%(user)s:%(password)s@%(host)s:%(port)s/%(db)s' %
    POSTGRES
)
