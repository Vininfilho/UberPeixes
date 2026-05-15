from flask import Blueprint, request, session, redirect, url_for, render_template
from werkzeug.security import check_password_hash
from script.utils.bd import supabase

login_bp = Blueprint('login', __name__)

@login_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        senha = request.form.get('senha')

        if not email or not senha:
            return render_template('login.html', erro="Preencha email e senha")

        try:
            response = supabase.table('users').select('*').eq('email', email).execute()
        except Exception:
            return render_template('login.html', erro="Erro ao conectar ao banco de dados")

        if not response.data:
            return render_template('login.html', erro="Usuário não encontrado")

        user = response.data[0]
        stored_password = user.get('password_hash')
        if not stored_password:
            return render_template('login.html', erro="Senha incorreta")

        if not (check_password_hash(stored_password, senha) or stored_password == senha):
            return render_template('login.html', erro="Senha incorreta")

        # Login bem-sucedido → salva sessão
        session['user_id'] = user['id']
        session['user_name'] = user['name']

        # Redireciona para backoffice
        return redirect(url_for('backoffice'))

    # Se for GET, apenas mostra o formulário
    return render_template('login.html')
