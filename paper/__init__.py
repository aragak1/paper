# -*- coding: utf-8 -*-
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
import sys
reload(sys)
sys.setdefaultencoding('utf8')

app = Flask(__name__)
admin = Admin(app, name='Paper')

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:253014@localhost:3306/paper?charset=utf8'
app.secret_key = 'mC\xf1_\x07`c\xc0\xbcu/WNP\xc6$\x96\xd4r\xc4&\x99\xf1X'

db = SQLAlchemy(app)

import paper.controller.front
import paper.controller.user
import paper.controller.api
import paper.controller.admin
