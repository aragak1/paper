# -*- coding: utf-8 -*-
from flask import session
from flask_admin import Admin, AdminIndexView
from flask_admin.contrib.sqla import ModelView
from flask_admin.contrib.fileadmin import FileAdmin
from paper import app, db
from paper.model.users import Users
from paper.model.companies import Companies
import os


class CommonView(ModelView):
    def is_accessible(self):
        return True  # if session.get('admin') else False


class UserView(CommonView):
    can_delete = False
    can_create = False
    can_edit = False

    column_labels = {
        'username': '用户名',
        'email': '邮箱',
        'admin': '管理员',
        'vip': 'VIP会员'
    }

    column_list = ['username', 'admin', 'vip', 'email']
    column_editable_list = ['admin', 'vip']


class CompanyView(CommonView):
    can_delete = False
    can_create = False

    column_labels = {
        'company_name': '公司名称',
        'introduction': '简介',
        'picture': '图片路径'
    }

    column_list = ['company_name', 'introduction', 'picture']

admin = Admin(app, name='Paper', index_view=AdminIndexView(name='导航', url='/paper_admin'))
admin.add_view(UserView(Users, db.session, name='用户'))
admin.add_view(CompanyView(Companies, db.session, '公司'))

company_pic_path = os.path.join(os.path.dirname(__file__)[0:-10], 'static/img/company')
admin.add_view(FileAdmin(company_pic_path, '/static/img/company/', name='公司图片'))


