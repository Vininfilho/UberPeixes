# UberPeixes

Projeto web em Flask para o controle de produtos e categorias de uma peixaria.

## Estrutura do projeto

- `script/`
  - `app.py` - aplicação Flask principal
  - `requirements.txt` - dependências Python
  - `models/` - modelos de dados
  - `routes/` - rotas da aplicação
  - `utils/` - utilitários
- `static/` - arquivos estáticos (CSS, JS, imagens)
- `templates/` - páginas HTML

## Como executar

1. Crie um ambiente virtual Python:
   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```

2. Instale as dependências:
   ```powershell
   pip install -r script\requirements.txt
   ```

3. Execute a aplicação:
   ```powershell
   python script\app.py
   ```

4. Acesse no navegador:
   ```text
   http://127.0.0.1:5000
   ```

## Git

O projeto já está inicializado com Git localmente.

Se ainda não adicionou o remoto, use:

```powershell
cd "C:\Users\Cliente\Desktop\UberPeixes"
git remote add origin https://github.com/SEU_USUARIO/UberPeixes.git
git push -u origin master
```

Se quiser usar `main` como branch principal:

```powershell
git branch -M main
git push -u origin main
```

## .gitignore

Arquivos ignorados:
- `__pycache__/`
- `.venv/`
- `.env`
- arquivos de editor
- logs
- arquivos de sistema
