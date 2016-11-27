# _*_ coding:utf8 _*_
from paper import db
from hashlib import md5


class Users(db.Model):
    __tablename__ = 'users'
    __salt = 'sYmFMqmj0955A7ns'

    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(16), unique=True)
    password = db.Column(db.String(32))
    email = db.Column(db.String(120), unique=True)
    status = db.Column(db.Integer)
    admin = db.Column(db.Integer)
    vip = db.Column(db.Integer)

    @staticmethod
    def __hash(password):
        m = md5()
        m.update(password)
        return m.hexdigest()

    @staticmethod
    def add_user(username, password, email, status=1, admin=0, vip=0):
        user = Users(username=username,
                     password=Users.__hash(password + Users.__salt),
                     email=email,
                     status=status,
                     admin=admin,
                     vip=vip)
        db.session.add(user)
        db.session.commit()

    @staticmethod
    def valid(username, password):
        users = Users.query.filter_by(username=username)
        if users.count():
            if users.first().password == Users.__hash(password + Users.__salt):
                return True
        return False

    @staticmethod
    def admin_valid(username, password):
        users = Users.query.filter_by(username=username)
        if users.count():
            if users.first().password == Users.__hash(password + Users.__salt) and users.first().admin:
                return True
        return False

    @staticmethod
    def existed(account, type_):
        if type_ == 'email':
            return True if Users.query.filter_by(email=account).count() else False
        return True if Users.query.filter_by(username=account).count() else False

    @staticmethod
    def get_user(username):
        return Users.query.filter_by(username=username).first()



