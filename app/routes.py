import sys
from app import app
from flask import render_template, request, flash, redirect
import csv
from .classes import *
from .csv_uses import *

@app.route("/")
@app.route("/index/")
def index():
    return render_template('index.html')

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
            substituir_csv([i[0],i[1],i[2],i[3],i[4]])
            return redirect("/index")
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
        if linha[2]==email:
            flash("Insira um usuário diferente!")
            return redirect("/registrar")
    else:
        escrever_csv([telefone,nome,email,senha,endereco])
        return ("Registrado com sucesso!")

@app.route("/atendimento")
def atendimento():
    return render_template("atendimento.html")
   
@app.route("/fisioterapia")
def selecionar1():
    return render_template("fisioterapia.html")

@app.route("/botox")
def selecionar2():
    return render_template("botox.html")

@app.route("/depilacao")
def selecionar3():
    return render_template("depilacao.html")