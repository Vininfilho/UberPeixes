from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash
from script.utils.bd import supabase

register_bp = Blueprint('register', __name__)

@register_bp.route('/register', methods=['POST'])
def register():
    name = request.form.get('name')
    email = request.form.get('email')
    senha = request.form.get('senha')

    senha_hash = generate_password_hash(senha)
    supabase.table('users').insert({
        'name': name,
        'email': email,
        'password_hash': senha_hash
    }).execute()

    return jsonify({'mensagem': 'Usuário registrado com sucesso'})
