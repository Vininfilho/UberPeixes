import os
from flask import Flask, render_template, session, redirect, url_for
from dotenv import load_dotenv
from script.routes import register_blueprints

# Carrega variáveis do .env
load_dotenv()

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "chave-padrao-local")

# Registra todos os blueprints (login, logout, register, produtos)
register_blueprints(app)

# Página inicial
@app.route('/')
@app.route('/home')
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

# Página de Backoffice (só acessível após login)
@app.route('/backoffice')
def backoffice():
    if not session.get('user_id'):
        return redirect(url_for('login.login'))
    return render_template('backoffice.html')

if __name__ == '__main__':
    app.run(debug=True)
