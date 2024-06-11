import pandas as pd
from flask import Flask, jsonify


app = Flask(__name__)

# Tente ler o arquivo CSV

@app.route('/')
def index():
    return '<h1>Olá, mundo!</h1>'


@app.route('/livros')
def livro():
    dados  =  pd.read_csv('C:/Users/blues/Downloads/teste-0/api/livros.csv')
    todos =  dados['LIVRO']
    return jsonify({todos})
        # print(n)
    
        
@app.route('/autor')
def autor():
    dados  =  pd.read_csv('C:/Users/blues/Downloads/teste-0/api/livros.csv')
    todos =  dados['AUTOR']    
    return jsonify({todos})


    
@app.route('/ano')
def ano():
    dados  =  pd.read_csv('C:/Users/blues/Downloads/teste-0/api/livros.csv')
    todos =  dados['ANO']
    return jsonify({todos})
        

@app.run('host = 'https://minhaapi.netlify.app/')
            


if __name__ == '__main__':
    app.run(debug=True)
