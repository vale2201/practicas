from flask import Flask, render_template, request, redirect, flash,url_for
import controlador_juegos
from markupsafe import escape

app = Flask(__name__)



@app.route('/')
def index():
    return 'Index Page'

@app.route("/agenda")
def juegos():
    juegos = controlador_juegos.obtener_juegos()
    return render_template("juegos.html", juegos=juegos)
@app.route('/p1')
def p1():
    return 'Hello, esta es la primera pagina'


@app.route('/user/<username>')
def profile(username):
    return '{}\'s profile'.format(escape(username))

# Iniciar el servidor
if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000, debug=True)




 