from flask import Flask
from flask_sqlalchemy import SQLAlchemy

import time

app = Flask(__name__)

db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = "User"
    ID = db.Column(db.Integer, primary_key=True)
    UserName = db.Column(db.String(50))
    Passwd = db.Column(db.String(50))
    Level = db.Column(db.Integer)

    def __str__(self):
        return self.UserName
    
    def __init__(self, **kwargs):
        super().__init__()
        if(not len(kwargs) == 0):
            self.ID = kwargs.get('ID')
            self.UserName = kwargs.get('UserName')
            self.Passwd = kwargs.get('Passwd')
            self.Level = kwargs.get('Level')


class Msg(db.Model):
    __tablename__ = 'Msg'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50))
    msg = db.Column(db.Text(10000))
    time = db.Column(db.DateTime)

    def __str__(self):
        return  '=' * 35 \
                + '\n' + '【' + self.username + '】 --> ' + self.time \
                + '\n' + '=' * 35  \
                + '\n' + self.msg

    def __init__(self, *args):
        if(len(args) != 0):
           self.username, self.msg = args
           self.time = time.strftime('%y-%m-%d %H:%M:%S', time.localtime(time.time()))

