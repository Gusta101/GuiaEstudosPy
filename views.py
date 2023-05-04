from flask import render_template
from main import app
from models import Estudo
from helpers import le_arquivo, escreve_arquivo, adiciona_conteudo

@app.route("/")
def index():
    save_dict = le_arquivo()
    estudo_atual = Estudo(save_dict)
    return render_template("index.html",
                           titulo="Guia de Estudos",
                           turno=estudo_atual.turno,
                           materias=estudo_atual.ciclo,
                           conteudo_revisao=estudo_atual.revisao)

@app.route("/novo")
def novo():
    # [[mat1, mat2, mat3], [mat4, mat5, mat6]]
    return render_template('criar.html', titulo='Criação de Plano')

@app.route("/criar")
def criar():
    return render_template('index')