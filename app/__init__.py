from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

import sentry_sdk
from sentry_sdk.integrations.flask import FlaskIntegration
from app import settings
from werkzeug.exceptions import HTTPException


class BaseRestApiException(Exception):
    # hack to ignore api exceptions from sending to sentry
    # and avoiding circular dependency
    pass


def create_app():
    sentry_sdk.init(
        dsn=settings.SENTRY_DSN,
        ignore_errors=[HTTPException, BaseRestApiException],
        integrations=[FlaskIntegration()],
        environment=settings.ENV
    )
    app = Flask(__name__)
    app.config.from_object(settings)
    app.name = app.config["APP_NAME"]
    app.config["SECRET_KEY"] = "you-will-never-guess"
    return app


app = create_app()
app.url_map.strict_slashes = False
api = Api(app)
db = SQLAlchemy(app)

__import__('app.urls')
__import__('app.models')