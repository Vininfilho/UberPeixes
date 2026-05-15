from flask import Flask, render_template
from script.utils.bd import supabase

app = Flask(__name__)

#Login
@app.route('/login')
def login():
    return render_template('login.html')

# Página inicial
@app.route('/')
def home():
    return render_template('home.html')

# Página de produtos
@app.route('/produtos')
def produtos():
    return render_template('produtos.html')

# Página "Sobre Nós"
@app.route('/sobre')
def sobre():
    return render_template('sobre.html')

# Página de contato
@app.route('/contato')
def contato():
    return render_template('contato.html')

# Página de Categoria
@app.route('/cadastro_categoria')
def cadastro_categoria():
    return render_template('cadastro_categoria.html')

# Página de Produto 
@app.route('/cadastro_produto')
def cadastro_produto():
    return render_template('cadastro_produto.html')

# Página de Backoffice
@app.route('/backoffice')
def backoffice():
    return render_template('backoffice.html')

if __name__ == '__main__':
    app.run(debug=True)
