from flask import Flask
app = Flask(__name__)


@app.route('/')
def index():
    return 'Index Page creo'

@app.route('/hello')
def hello():
    return 'Hello, vale'

if __name__ == "__main__":
    app.run()