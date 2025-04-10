from flask import Flask, render_template, request
import random 
import string 

app = Flask(__name__)

def gerar_senha(tamanho=12, incluir_maiusculas=True, incluir_numeros=True, incluir_simbolos=True): 
    caracteres = string.ascii_lowercase  # Sempre inclui minúsculas
    if incluir_maiusculas:
        caracteres += string.ascii_uppercase
    if incluir_numeros:
        caracteres += string.digits
    if incluir_simbolos:
        caracteres += string.punctuation
    
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha

@app.route("/", methods=["GET", "POST"])
def index():
    senha_gerada = ""
    if request.method == "POST":
        tamanho = int(request.form["tamanho"])
        maiusculas = "maiusculas" in request.form
        numeros = "numeros" in request.form
        simbolos = "simbolos" in request.form
        
        senha_gerada = gerar_senha(tamanho, maiusculas, numeros, simbolos)
    
    return render_template("index.html", senha=senha_gerada)

if __name__ == "__main__":
    app.run(debug=True)
