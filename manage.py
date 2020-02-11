from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from main import app, db
from models.user import User
from models.address import Address

from routes.main import routes_main
from routes.user import routes_users

app.register_blueprint(routes_main, url_prefix='/')
app.register_blueprint(routes_users, url_prefix='/api')

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command("db", MigrateCommand)

if __name__=='__main__':
    manager.run()