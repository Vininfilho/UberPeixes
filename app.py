import os
from flask import Flask, render_template, session, redirect, url_for, request
from dotenv import load_dotenv
from script.routes import register_blueprints
from script.utils.bd import supabase

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

# Página de produtos (ajustada para buscar no banco)
@app.route('/produtos')
def produtos():
    # Busca produtos
    produtos_resp = supabase.table('products').select('id, name, price').order('id', desc=False).execute()
    produtos = produtos_resp.data if produtos_resp.data else []

    # Busca imagens principais
    imagens_resp = supabase.table('produto_imagens').select('produto_id, url, principal, ordem').execute()
    imagens = {img['produto_id']: img for img in imagens_resp.data if img['principal'] or img['ordem'] == 1}

    # Junta produto + imagem
    for p in produtos:
        p['imagem_url'] = imagens.get(p['id'], {}).get('url', '/static/images/no-image.png')

    return render_template('produtos.html', produtos=produtos)

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
    if not session.get('user_id'):
        return redirect(url_for('login.login'))

    response = supabase.table('categories').select('*').order('id', desc=False).execute()
    categorias = response.data if response.data else []
    return render_template('lista_categoria.html', categorias=categorias)

@app.route('/cadastro_categoria/detail', methods=['GET', 'POST'])
@app.route('/cadastro_categoria/detail/<int:categoria_id>', methods=['GET', 'POST'])
def categoria_detail(categoria_id=None):
    if not session.get('user_id'):
        return redirect(url_for('login.login'))

    categoria = None
    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        description = request.form.get('description', '').strip()

        if categoria_id:
            supabase.table('categories').update({'name': name, 'description': description}).eq('id', categoria_id).execute()
        else:
            supabase.table('categories').insert([{'name': name, 'description': description}]).execute()

        return redirect(url_for('cadastro_categoria'))

    if categoria_id:
        response = supabase.table('categories').select('*').eq('id', categoria_id).single().execute()
        categoria = response.data if response.data else None

    return render_template('cadastro_categoria.html', categoria=categoria)

# Página de Produto - listagem
@app.route('/cadastro_produto')
def cadastro_produto():
    if not session.get('user_id'):
        return redirect(url_for('login.login'))

    categories_resp = supabase.table('categories').select('id,name').order('id', desc=False).execute()
    brands_resp = supabase.table('brands').select('id,name').order('id', desc=False).execute()
    types_resp = supabase.table('product_types').select('id,name').order('id', desc=False).execute()
    categories = categories_resp.data or []
    brands = brands_resp.data or []
    types = types_resp.data or []

    produto_resp = supabase.table('products').select('*').order('id', desc=False).execute()
    produtos = produto_resp.data or []
    category_map = {item['id']: item['name'] for item in categories}
    brand_map = {item['id']: item['name'] for item in brands}
    type_map = {item['id']: item['name'] for item in types}

    return render_template(
        'lista_produto.html',
        produtos=produtos,
        category_map=category_map,
        brand_map=brand_map,
        type_map=type_map,
    )

@app.route('/cadastro_produto/detail', methods=['GET', 'POST'])
@app.route('/cadastro_produto/detail/<int:produto_id>', methods=['GET', 'POST'])
def produto_detail(produto_id=None):
    if not session.get('user_id'):
        return redirect(url_for('login.login'))

    categories_resp = supabase.table('categories').select('id,name').order('id', desc=False).execute()
    brands_resp = supabase.table('brands').select('id,name').order('id', desc=False).execute()
    types_resp = supabase.table('product_types').select('id,name').order('id', desc=False).execute()
    categories = categories_resp.data or []
    brands = brands_resp.data or []
    types = types_resp.data or []

    produto = None
    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        description = request.form.get('description', '').strip()
        price = request.form.get('price', '0') or '0'
        stock_quantity = request.form.get('stock_quantity', '0') or '0'
        category_id = request.form.get('category_id') or None
        brand_id = request.form.get('brand_id') or None
        type_id = request.form.get('type_id') or None

        produto_data = {
            'name': name,
            'description': description,
            'price': float(price),
            'stock_quantity': int(stock_quantity),
            'category_id': int(category_id) if category_id else None,
            'brand_id': int(brand_id) if brand_id else None,
            'type_id': int(type_id) if type_id else None,
        }

        if produto_id:
            supabase.table('products').update(produto_data).eq('id', produto_id).execute()
        else:
            supabase.table('products').insert([produto_data]).execute()

        return redirect(url_for('cadastro_produto'))

    if produto_id:
        response = supabase.table('products').select('*').eq('id', produto_id).single().execute()
        produto = response.data if response.data else None

    return render_template(
        'cadastro_produto.html',
        produto=produto,
        categories=categories,
        brands=brands,
        types=types,
    )

# Página de Backoffice (só acessível após login)
@app.route('/backoffice')
def backoffice():
    if not session.get('user_id'):
        return redirect(url_for('login.login'))
    return render_template('backoffice.html')

if __name__ == '__main__':
    app.run(debug=True)
