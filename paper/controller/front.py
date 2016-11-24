from paper import app
from flask import session, render_template


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/companies')
def companies():
    return render_template('companies.html')


@app.route('/paper')
def paper():
    return render_template('paper.html')
