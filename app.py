from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def pagina_principal():
    return render_template("principal.html")

@app.route("/Sobre")
def pagina_sobre():
    return render_template("/sobre.html")

app.run(debug=True)