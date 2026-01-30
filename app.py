from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route("/")
def pagina_principal():
    return render_template("principal.html")

@app.route("/Sobre", methods=["GET"])
def pagina_sobre():
    return render_template("sobre.html")

@app.route("/Login", methods=["GET"])
def pagina_login():
    return render_template("login.html")

@app.route("/login", methods=["POST"])
def login_post():
   usuario = request.form.get("nome")
   senha = request.form.get("senha")

   if usuario == "godofredo" and senha == "godofredo123":
    return "Você acessou a pagina"
   else:
      return render_template ("login.html", erro = "acesso negado")
   
@app.route("/Comentarios")
def pagina_comentarios():
   return render_template("comentarios.html")


app.run(debug=True)