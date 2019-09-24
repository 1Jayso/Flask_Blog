from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
import flask_whooshalchemyplus

app = Flask(__name__)

app.config['SECRET_KEY'] = 'c2cf55a7b26cf64dbe60700f89c74650'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
app.config["DEBUG"] = True
app.config['WHOOSH_BASE'] = 'whoosh'
db = SQLAlchemy(app)
flask_whooshalchemyplus.init_app(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = "login"
login_manager.login_message_category = "info"




from flaskblog import routes
