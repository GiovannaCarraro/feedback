from flask import Flask, render_template, request, redirect

app = Flask(__name__)

app.secret_key = "banana"

lista_comentarios = []

@app.route("/")
def pagina_principal():
    return render_template("principal.html")

@app.route("/sobre", methods=["GET"])
def pagina_sobre():
    return render_template("sobre.html")

@app.route("/login", methods=["GET"])
def pagina_login():
    return render_template("login.html")

@app.route("/login", methods=["POST"])
def login_post():
   usuario = request.form.get("nome")
   senha = request.form.get("senha")

   if usuario == "godofredo" and senha == "godofredo123":
    return redirect("/comentarios")
   else:
      return render_template ("login.html", erro = "acesso negado")
   
@app.route("/comentarios", methods=["GET"])
def pagina_comentarios():
   return render_template("comentarios.html", lista_comentario = lista_comentarios)

@app.route("/adicionar_comentario", methods=["POST"])
def adicionar_comentario():
   comentario = request.form.get("comentario")
   lista_comentarios.append(comentario)
   print(lista_comentarios)
   return redirect("/comentarios")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)