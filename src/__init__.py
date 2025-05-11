from flask import Flask
from .db_con import db, migrate
from .ext import bcrypt
from .conf import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    bcrypt.init_app(app)
    
    
    # Register blueprints
    from .routes.user import user_bp
    app.register_blueprint(user_bp, url_prefix='/user')
    
    return app