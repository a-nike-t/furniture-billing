from flask_script import Manager, Shell, Server
from flask_migrate import Migrate, MigrateCommand
from app import app, db


def _make_context():
    return dict(app=app)


migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)
server = Server(host=app.config["HOST_URL"], port=app.config["HOST_PORT"])
manager.add_command("runserver", server)
manager.add_command("shell", Shell(make_context=_make_context))


if __name__ == "__main__":
    manager.run()