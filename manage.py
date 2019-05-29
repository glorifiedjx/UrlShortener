#! /usr/bin/env python

from URLShortener import app, db
from  URLShortener.models import WebUrl
from flask_script import Manager, prompt_bool

manager = Manager(app)

@manager.command
def initdb():
    db.create_all()
    print('Initialized the database')

@manager.command
def dropdb():
    if prompt_bool("All your data in db will be lost. is that fine?"):
        db.drop_all()
        print('Dropped the database')

if __name__ == '__main__':
    manager.run()
