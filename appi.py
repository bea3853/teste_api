# app.py
import pandas as pd
from flask import Flask, jsonify

app = Flask(__name__)

# Função para ler o arquivo CSV
def ler_csv():
    return pd.read_csv('C:/Users/blues/Downloads/teste-0/api/livros.csv')

@app.route('/')
def index():
    return '<h1>Olá, mundo!</h1>'

@app.route('/livros')
def livro():
    dados = ler_csv()
    todos = dados['LIVRO'].tolist()
    return jsonify(todos)

@app.route('/autor')
def autor():
    dados = ler_csv()
    todos = dados['AUTOR'].tolist()
    return jsonify(todos)





@app.route('/ano')
def ano():
    dados = ler_csv()
    todos = dados['ANO'].tolist()
    return jsonify(todos)






if __name__ == '__main__':
    app.run(debug=True)
