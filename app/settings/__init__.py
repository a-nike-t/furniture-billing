import os

ENV = os.getenv("ENV", "local")
if ENV == "production":
    from .production import *  # NOQA
elif ENV == "staging":
    from .staging import *  # NOQA
else:
    from .local import *  # NOQA
