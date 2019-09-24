
from flaskblog import app
# import secrets
# secrets.token_hex(16)
# The above code is use to generate a secret key(byte string)


#! /usr/bin/env python
from flask_script import Manager, prompt_bool
from flaskblog.models import User, Post
from flaskblog import app, db
from flask_migrate import Migrate, MigrateCommand


migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)


@manager.command
def insert_data():
    
    joseph = User(username="Jokoto", email="jokoto@example.com", password="test")
    db.session.add(joseph)
    
    def add_post(title, content):
        db.session.add(Post(title=title, content=content, author=joseph))

    add_post("Programming Training", "Pluralsight. Hardcore developer training.")
    add_post("Why I love python", "Python - my favorite language")
    add_post("Building web apps with flask", "Flask: Web development one drop at a time.")
    add_post("Reddit", "Reddit. Frontpage of the internet")
    add_post("SqlAlchemy", "Nice ORM framework")

    arjen = User(username="arjen", email="arjen@robben.nl", password="test")
    db.session.add(arjen)
    db.session.commit()


    print('Initialized the database')

@manager.command
def dropdb():
    if prompt_bool(
        "Are you sure you want to lose all your data"):
        db.drop_all()
        print('Dropped the database')

if __name__ == '__main__':
    manager.run()
    




