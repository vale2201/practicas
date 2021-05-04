# Importas los paquetes necesarios
from flask import Flask, render_template, request, Response, redirect, flash, url_for
import controlador
from markupsafe import escape

# Aqui preparas flask para presentar las vistas
app = Flask(__name__, static_url_path='/static')

# Preparas tus rutas
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/estructura')
def mestra():
    return render_template("estructura.html")

@app.route("/agenda")
def agen():
    agen = controlador.obtener_agen()
    return render_template("agen.html", agen=agen)

@app.route('/juegos')
def juegos():
    juegos = controlador.obtener_J()
    return render_template("juegos.html", juegos=juegos)

@app.route('/user/<username>')
def profile(username):
    return '{}\'s profile'.format(escape(username))

# Iniciar el servidor
if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000, debug=True)

