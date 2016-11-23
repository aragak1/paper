from paper import app
from flask import session


@app.route('/')
def index():
    if session['username']:
        return 'welcome %s' % session['username']
    return 'hello world!'
