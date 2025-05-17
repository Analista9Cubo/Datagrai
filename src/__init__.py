from flask import Flask
from .db_con import db, migrate
from .ext import bcrypt, jwt
from .conf import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    bcrypt.init_app(app)
    jwt.init_app(app)
    
    # Register blueprints
    from .routes.user import user_bp
    from .routes.readings import read_bp
    from .routes.roles import rol_bp
    from .routes.alerts import alert_bp
    app.register_blueprint(user_bp, url_prefix='/user')
    app.register_blueprint(read_bp, url_prefix='/read')
    app.register_blueprint(rol_bp, url_prefix='/rol')
    app.register_blueprint(alert_bp, url_prefix='/alert')
    
    return app