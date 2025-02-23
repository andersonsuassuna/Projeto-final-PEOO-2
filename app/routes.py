from app import app
from flask import render_template
from flask import request

@app.route("/", defaults={"nome":"usuário"})
@app.route("/index/", defaults={"nome":"usuário"})
@app.route("/index/<nome>")
def index(nome):
    dicionario={"nome":nome,
                "idade":"17"}
    return render_template('index.html', **dicionario)

@app.route("/contato")
def contato():
    return render_template("contato.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/autenticar", methods=["GET"])
def autenticar():
    usuario=request.args.get("usuário")
    senha=request.args.get("senha")
    return f"usuário: {usuario} e senha: {senha}"