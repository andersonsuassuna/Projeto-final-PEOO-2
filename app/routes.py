import sys
from app import app
from flask import render_template, request, flash, redirect
import csv
from .classes import *
from .csv_uses import *

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

@app.route("/autenticar", methods=["POST"])
def autenticar():
    email=request.form.get("email")
    senha=request.form.get("senha")
    lista=gerar_lista()
    for i in lista:
        if email==i[2] and senha==i[3]:
            return f"usuário: {email} e senha: {senha}"
    flash("Dados inválidos!")
    return redirect("/login")

@app.route("/registrar")
def registrar():
    return render_template("registrar.html")

@app.route("/registro", methods=["POST"])
def registro():
    telefone=request.form.get("telefone")
    nome=request.form.get("nome")
    email=request.form.get("email")
    senha=request.form.get("senha")
    endereco=request.form.get("endereco")
    for linha in (gerar_lista()):
        if linha[0]==email:
            flash("Insira um usuário diferente!")
            return redirect("/registrar")
    else:
        escrever_csv([telefone,nome,email,senha,endereco])
        return ("Registrado com sucesso!")