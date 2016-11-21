from paper import app


@app.route('/')
def index():
    return 'hello world!'
