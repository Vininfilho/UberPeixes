from flask import Blueprint, render_template, session, redirect, url_for

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
    return render_template('cadastro_marca.html')

@backoffice_bp.route('/cadastro_tipo_produto')
def cadastro_tipo_produto():
    if not session.get('user_id'):
        return redirect(url_for('login.login'))
    return render_template('cadastro_tipo_produto.html')

@backoffice_bp.route('/cadastro_atributo')
def cadastro_atributo():
    if not session.get('user_id'):
        return redirect(url_for('login.login'))
    return render_template('cadastro_atributo.html')

@backoffice_bp.route('/cadastro_imagem_produto')
def cadastro_imagem_produto():
    if not session.get('user_id'):
        return redirect(url_for('login.login'))
    return render_template('cadastro_imagem_produto.html')

@backoffice_bp.route('/cadastro_usuario')
def cadastro_usuario():
    if not session.get('user_id'):
        return redirect(url_for('login.login'))
    return render_template('cadastro_usuario.html')

@backoffice_bp.route('/cadastro_pedido')
def cadastro_pedido():
    if not session.get('user_id'):
        return redirect(url_for('login.login'))
    return render_template('cadastro_pedido.html')

@backoffice_bp.route('/cadastro_item_pedido')
def cadastro_item_pedido():
    if not session.get('user_id'):
        return redirect(url_for('login.login'))
    return render_template('cadastro_item_pedido.html')
