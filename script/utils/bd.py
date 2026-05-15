import os
from supabase import create_client, Client
from dotenv import load_dotenv

# Carrega variáveis do arquivo .env (apenas em ambiente local)
load_dotenv()

# Lê variáveis de ambiente (funciona no Render e local)
SUPABASE_URL = os.environ.get("SUPABASE_URL")
SUPABASE_KEY = os.environ.get("SUPABASE_KEY")

if not SUPABASE_URL or not SUPABASE_KEY:
    raise ValueError("SUPABASE_URL ou SUPABASE_KEY não foram definidos.")

# Cria cliente Supabase
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)
