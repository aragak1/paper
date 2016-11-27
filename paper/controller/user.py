# -*- coding: utf8 -*-
from paper import app
from flask import render_template, redirect, request, session
from ..model.users import Users
from ..controller.util import valid_email


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        if Users.valid(username, request.form.get('password')):
            session['username'] = username
            return 'success'
        return 'failed'
    return render_template('login.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        re_password = request.form.get('re_password')
        email = request.form.get('email')
        if not username or not password or not email:
            return 'error'
        if password != re_password:
            return '两次输入的密码不一致！'
        elif Users.existed(username, type_='username'):
            return '用户名已存在！'
        elif Users.existed(email, type_='email'):
            return '邮箱已被使用！'
        elif not valid_email(email):
            return '邮箱格式错误！'
        Users.add_user(username=username, password=password, email=email)
        return 'success'

    return render_template('register.html')


@app.route('/logout')
def logout():
    if session.get('username'):
        session.pop('username')
    if session.get('admin'):
        session.pop('admin')
    return redirect('/')
