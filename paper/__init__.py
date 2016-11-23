# -*- coding: utf-8 -*-
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import sys
reload(sys)
sys.setdefaultencoding('utf8')

app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:253014@localhost:3306/paper?charset=utf8'
app.secret_key = 'mC\xf1_\x07`c\xc0\xbcu/WNP\xc6$\x96\xd4r\xc4&\x99\xf1X'

db = SQLAlchemy(app)

import paper.controller.index
import paper.controller.user
import paper.controller.api
