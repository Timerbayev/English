from flask import Flask
from config import Configuration
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_wtf.csrf import CSRFProtect
from admin.admin import admin

# __name__ name of a current file
app = Flask(__name__)
app.config.from_object(Configuration)
app.register_blueprint(admin, url_prefix='/admin')
db = SQLAlchemy(app)
migrate = Migrate(app, db)