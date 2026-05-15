from flask import Blueprint, jsonify
from script.utils.bd import supabase

produtos_bp = Blueprint('produtos', __name__)

@produtos_bp.route('/api/produtos', methods=['GET'])
def listar_produtos_api():
    response = supabase.table('products').select('*').execute()
    return jsonify(response.data)
