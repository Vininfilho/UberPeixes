from flask import Blueprint, render_template
from script.utils.bd import supabase

site_bp = Blueprint('site', __name__)

@site_bp.route('/produtos')
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
