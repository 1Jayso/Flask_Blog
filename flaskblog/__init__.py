import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
import flask_whooshalchemy
from flask_mail import Mail


app = Flask(__name__)

app.config['SECRET_KEY'] = 'c2cf55a7b26cf64dbe60700f89c74650'
# SQLAlchemy configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
app.config["DEBUG"] = True
app.config['WHOOSH_BASE'] = 'whoosh'
db = SQLAlchemy(app)
# Flask bcrypt instance
bcrypt = Bcrypt(app)
login_manager.login_view = "login"
login_manager.login_message_category = "info"

mail_settings = {
    "MAIL_SERVER": 'smtp.gmail.com',
    "MAIL_PORT": 465,
    "MAIL_USE_TLS": False,
    "MAIL_USE_SSL": True,
    "MAIL_USERNAME":"#",
    
    "MAIL_PASSWORD": "#"
}

app.config.update(mail_settings)
mail = Mail(app)




from flaskblog import routes
