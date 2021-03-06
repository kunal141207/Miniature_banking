from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from app import create_app
from config import FlaskConfig

app = create_app(FlaskConfig)

from app import db
migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()
