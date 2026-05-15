from flask import Blueprint
from script.routes.login import login_bp
from script.routes.logout import logout_bp
from script.routes.register import register_bp
from script.routes.produtos import produtos_bp
from script.routes.backoffice import backoffice_bp  

def register_blueprints(app):
    app.register_blueprint(login_bp)
    app.register_blueprint(logout_bp)
    app.register_blueprint(register_bp)
    app.register_blueprint(produtos_bp)
    app.register_blueprint(backoffice_bp) 
