from flask import Blueprint, render_template, session, redirect, url_for, request
from werkzeug.security import generate_password_hash
from script.utils.bd import supabase

backoffice_bp = Blueprint('backoffice', __name__)

@backoffice_bp.route('/backoffice')
def backoffice():
    if not session.get('user_id'):
        return redirect(url_for('login.login'))
    return render_template('backoffice.html')

@backoffice_bp.route('/cadastro_marca')
def cadastro_marca():
    if not session.get('user_id'):
        return redirect(url_for('login.login'))

    response = supabase.table('brands').select('*').order('id', desc=False).execute()
    marcas = response.data if response.data else []
    return render_template('lista_marca.html', marcas=marcas)

@backoffice_bp.route('/cadastro_marca/detail', methods=['GET', 'POST'])
@backoffice_bp.route('/cadastro_marca/detail/<int:marca_id>', methods=['GET', 'POST'])
def marca_detail(marca_id=None):
    if not session.get('user_id'):
        return redirect(url_for('login.login'))

    marca = None
    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        country = request.form.get('country', '').strip()

        if marca_id:
            supabase.table('brands').update({'name': name, 'country': country}).eq('id', marca_id).execute()
        else:
            supabase.table('brands').insert([{'name': name, 'country': country}]).execute()

        return redirect(url_for('backoffice.cadastro_marca'))

    if marca_id:
        response = supabase.table('brands').select('*').eq('id', marca_id).single().execute()
        marca = response.data if response.data else None

    return render_template('cadastro_marca.html', marca=marca)

@backoffice_bp.route('/cadastro_tipo_produto')
def cadastro_tipo_produto():
    if not session.get('user_id'):
        return redirect(url_for('login.login'))

    response = supabase.table('product_types').select('*').order('id', desc=False).execute()
    tipos = response.data if response.data else []
    return render_template('lista_tipo_produto.html', tipos=tipos)

@backoffice_bp.route('/cadastro_tipo_produto/detail', methods=['GET', 'POST'])
@backoffice_bp.route('/cadastro_tipo_produto/detail/<int:tipo_id>', methods=['GET', 'POST'])
def tipo_produto_detail(tipo_id=None):
    if not session.get('user_id'):
        return redirect(url_for('login.login'))

    categories_resp = supabase.table('categories').select('id,name').order('id', desc=False).execute()
    categories = categories_resp.data if categories_resp.data else []
    tipo = None

    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        category_id = request.form.get('category_id') or None
        data = {
            'name': name,
            'category_id': int(category_id) if category_id else None,
        }

        if tipo_id:
            supabase.table('product_types').update(data).eq('id', tipo_id).execute()
        else:
            supabase.table('product_types').insert([data]).execute()

        return redirect(url_for('backoffice.cadastro_tipo_produto'))

    if tipo_id:
        response = supabase.table('product_types').select('*').eq('id', tipo_id).single().execute()
        tipo = response.data if response.data else None

    return render_template('cadastro_tipo_produto.html', tipo=tipo, categories=categories)

@backoffice_bp.route('/cadastro_atributo')
def cadastro_atributo():
    if not session.get('user_id'):
        return redirect(url_for('login.login'))

    produtos_resp = supabase.table('products').select('id,name').order('id', desc=False).execute()
    produtos = produtos_resp.data if produtos_resp.data else []
    atributos_resp = supabase.table('product_attributes').select('*').order('id', desc=False).execute()
    atributos = atributos_resp.data if atributos_resp.data else []
    return render_template('lista_atributo.html', atributos=atributos, produtos=produtos)

@backoffice_bp.route('/cadastro_atributo/detail', methods=['GET', 'POST'])
@backoffice_bp.route('/cadastro_atributo/detail/<int:atributo_id>', methods=['GET', 'POST'])
def atributo_detail(atributo_id=None):
    if not session.get('user_id'):
        return redirect(url_for('login.login'))

    produtos_resp = supabase.table('products').select('id,name').order('id', desc=False).execute()
    produtos = produtos_resp.data if produtos_resp.data else []
    atributo = None

    if request.method == 'POST':
        product_id = request.form.get('product_id') or None
        attribute_name = request.form.get('attribute_name', '').strip()
        attribute_value = request.form.get('attribute_value', '').strip()
        data = {
            'product_id': int(product_id) if product_id else None,
            'attribute_name': attribute_name,
            'attribute_value': attribute_value,
        }

        if atributo_id:
            supabase.table('product_attributes').update(data).eq('id', atributo_id).execute()
        else:
            supabase.table('product_attributes').insert([data]).execute()

        return redirect(url_for('backoffice.cadastro_atributo'))

    if atributo_id:
        response = supabase.table('product_attributes').select('*').eq('id', atributo_id).single().execute()
        atributo = response.data if response.data else None

    return render_template('cadastro_atributo.html', atributo=atributo, produtos=produtos)

@backoffice_bp.route('/cadastro_imagem_produto')
def cadastro_imagem_produto():
    if not session.get('user_id'):
        return redirect(url_for('login.login'))

    produtos_resp = supabase.table('products').select('id,name').order('id', desc=False).execute()
    produtos = produtos_resp.data if produtos_resp.data else []
    imagens_resp = supabase.table('produto_imagens').select('*').order('id', desc=False).execute()
    imagens = imagens_resp.data if imagens_resp.data else []
    return render_template('lista_imagem_produto.html', imagens=imagens, produtos=produtos)

@backoffice_bp.route('/cadastro_imagem_produto/detail', methods=['GET', 'POST'])
@backoffice_bp.route('/cadastro_imagem_produto/detail/<int:imagem_id>', methods=['GET', 'POST'])
def imagem_produto_detail(imagem_id=None):
    if not session.get('user_id'):
        return redirect(url_for('login.login'))

    produtos_resp = supabase.table('products').select('id,name').order('id', desc=False).execute()
    produtos = produtos_resp.data if produtos_resp.data else []
    imagem = None

    if request.method == 'POST':
        produto_id = request.form.get('produto_id') or None
        url = request.form.get('url', '').strip()
        nome_arquivo = request.form.get('nome_arquivo', '').strip()
        principal = request.form.get('principal') == 'on'
        ordem = request.form.get('ordem', '1') or '1'
        data = {
            'produto_id': int(produto_id) if produto_id else None,
            'url': url,
            'nome_arquivo': nome_arquivo,
            'principal': principal,
            'ordem': int(ordem),
        }

        if imagem_id:
            supabase.table('produto_imagens').update(data).eq('id', imagem_id).execute()
        else:
            supabase.table('produto_imagens').insert([data]).execute()

        return redirect(url_for('backoffice.cadastro_imagem_produto'))

    if imagem_id:
        response = supabase.table('produto_imagens').select('*').eq('id', imagem_id).single().execute()
        imagem = response.data if response.data else None

    return render_template('cadastro_imagem_produto.html', imagem=imagem, produtos=produtos)

@backoffice_bp.route('/cadastro_usuario')
def cadastro_usuario():
    if not session.get('user_id'):
        return redirect(url_for('login.login'))

    response = supabase.table('users').select('id, name, email, created_at').order('created_at', desc=False).execute()
    usuarios = response.data if response.data else []
    return render_template('lista_usuario.html', usuarios=usuarios)

@backoffice_bp.route('/cadastro_usuario/detail', methods=['GET', 'POST'])
@backoffice_bp.route('/cadastro_usuario/detail/<string:user_id>', methods=['GET', 'POST'])
def usuario_detail(user_id=None):
    if not session.get('user_id'):
        return redirect(url_for('login.login'))

    usuario = None
    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        email = request.form.get('email', '').strip()
        password = request.form.get('password', '').strip()

        data = {
            'name': name,
            'email': email,
        }
        if password:
            data['password_hash'] = generate_password_hash(password)

        if user_id:
            supabase.table('users').update(data).eq('id', user_id).execute()
        else:
            if password:
                supabase.table('users').insert([data]).execute()
            else:
                return render_template('cadastro_usuario.html', usuario=None, erro='Senha é obrigatória ao criar usuário')

        return redirect(url_for('backoffice.cadastro_usuario'))

    if user_id:
        response = supabase.table('users').select('id, name, email, created_at').eq('id', user_id).single().execute()
        usuario = response.data if response.data else None

    return render_template('cadastro_usuario.html', usuario=usuario)

@backoffice_bp.route('/cadastro_pedido')
def cadastro_pedido():
    if not session.get('user_id'):
        return redirect(url_for('login.login'))

    usuarios_resp = supabase.table('users').select('id,name,email').order('created_at', desc=False).execute()
    usuarios = usuarios_resp.data if usuarios_resp.data else []
    pedidos_resp = supabase.table('orders').select('*').order('id', desc=False).execute()
    pedidos = pedidos_resp.data if pedidos_resp.data else []
    return render_template('lista_pedido.html', pedidos=pedidos, usuarios=usuarios)

@backoffice_bp.route('/cadastro_pedido/detail', methods=['GET', 'POST'])
@backoffice_bp.route('/cadastro_pedido/detail/<int:pedido_id>', methods=['GET', 'POST'])
def pedido_detail(pedido_id=None):
    if not session.get('user_id'):
        return redirect(url_for('login.login'))

    usuarios_resp = supabase.table('users').select('id,name,email').order('created_at', desc=False).execute()
    usuarios = usuarios_resp.data if usuarios_resp.data else []
    pedido = None

    if request.method == 'POST':
        user_id = request.form.get('user_id') or None
        status = request.form.get('status', '').strip()
        total_price = request.form.get('total_price', '0') or '0'
        data = {
            'user_id': user_id,
            'status': status,
            'total_price': float(total_price),
        }

        if pedido_id:
            supabase.table('orders').update(data).eq('id', pedido_id).execute()
        else:
            supabase.table('orders').insert([data]).execute()

        return redirect(url_for('backoffice.cadastro_pedido'))

    if pedido_id:
        response = supabase.table('orders').select('*').eq('id', pedido_id).single().execute()
        pedido = response.data if response.data else None

    return render_template('cadastro_pedido.html', pedido=pedido, usuarios=usuarios)

@backoffice_bp.route('/cadastro_item_pedido')
def cadastro_item_pedido():
    if not session.get('user_id'):
        return redirect(url_for('login.login'))

    pedidos_resp = supabase.table('orders').select('id').order('id', desc=False).execute()
    produtos_resp = supabase.table('products').select('id,name').order('id', desc=False).execute()
    itens_resp = supabase.table('order_items').select('*').order('id', desc=False).execute()
    pedidos = pedidos_resp.data if pedidos_resp.data else []
    produtos = produtos_resp.data if produtos_resp.data else []
    itens = itens_resp.data if itens_resp.data else []
    return render_template('lista_item_pedido.html', itens=itens, pedidos=pedidos, produtos=produtos)

@backoffice_bp.route('/cadastro_item_pedido/detail', methods=['GET', 'POST'])
@backoffice_bp.route('/cadastro_item_pedido/detail/<int:item_id>', methods=['GET', 'POST'])
def item_pedido_detail(item_id=None):
    if not session.get('user_id'):
        return redirect(url_for('login.login'))

    pedidos_resp = supabase.table('orders').select('id').order('id', desc=False).execute()
    produtos_resp = supabase.table('products').select('id,name').order('id', desc=False).execute()
    pedidos = pedidos_resp.data if pedidos_resp.data else []
    produtos = produtos_resp.data if produtos_resp.data else []
    item = None

    if request.method == 'POST':
        order_id = request.form.get('order_id') or None
        product_id = request.form.get('product_id') or None
        quantity = request.form.get('quantity', '1') or '1'
        unit_price = request.form.get('unit_price', '0') or '0'
        data = {
            'order_id': int(order_id) if order_id else None,
            'product_id': int(product_id) if product_id else None,
            'quantity': int(quantity),
            'unit_price': float(unit_price),
        }

        if item_id:
            supabase.table('order_items').update(data).eq('id', item_id).execute()
        else:
            supabase.table('order_items').insert([data]).execute()

        return redirect(url_for('backoffice.cadastro_item_pedido'))

    if item_id:
        response = supabase.table('order_items').select('*').eq('id', item_id).single().execute()
        item = response.data if response.data else None

    return render_template('cadastro_item_pedido.html', item=item, pedidos=pedidos, produtos=produtos)
