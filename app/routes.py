from app import app
from flask import render_template

@app.route("/")
@app.route("/index")
def index():
    dicionario={"nome":"Anderson",
                "idade":"17"}
    return render_template('index.html', **dicionario)

@app.route("/contato")
def contato():
    return render_template("contato.html")