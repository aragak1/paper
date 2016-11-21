# _*_ coding:utf8 _*_
from paper import db


class User(db.Model):
    __tablename__ = 'users'

    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(16), unique=True)
    password = db.Column(db.String(32))
    email = db.Column(db.String(120), unique=True)
    status = db.Column(db.Integer)
    admin = db.Column(db.Integer)
    vip = db.Column(db.Integer)

    @staticmethod
    def add_user(username, password, email, status=1, admin=0, vip=0):
        user = User(username=username,
                    password=password,
                    email=email,
                    status=status,
                    admin=admin,
                    vip=vip)
        db.session.add(user)
        db.session.commit()
