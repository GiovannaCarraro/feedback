from flask import Flask, render_template, request, redirect, session


app = Flask(__name__)

app.secret_key = "chiclete"

lista_comentarios = []


@app.route("/")
def pag_index():
    return render_template("principal.html")

@app.route("/sobre")
def pag_sobre():
    return render_template("sobre.html")

@app.route("/login")
def pag_login():
    return render_template("login.html")

#rota dp login
@app.route("/login", methods = ["POST"])
def login_post():
    usuario = request.form.get("usuario")
    senha = request.form.get("senha")

    if usuario == "giovanna" and senha == "123":
        session["usuario"] = "123"
        return "Eita você acessou uma area restrita"
    else:
        return render_template("login.html", erro = "Acesso negado!")
    
# @app.route("/comentario")
# def pag_comentario():
#     return render_template("comentarios.html")

@app.route("/comentarios", methods = ["GET"])
def pag_comentario():
    if "usuario" in session:
        return render_template("comentarios.html", lista_comentarios_html = lista_comentarios)


@app.route("/adicionar", methods=["POST"])
def adicionar():
    comentario = request.form.get("comentario")
    lista_comentarios.append(comentario)
    print(lista_comentarios)
    return redirect("/comentarios") 

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=8080)