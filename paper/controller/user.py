# -*- coding: utf8 -*-
from paper import app
from flask import render_template


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/user', methods=['POST'])
def add_user():
    pass


@app.route('/register')
def register():
    return render_template('register.html')


@app.route('/logout')
def logout():
    pass
