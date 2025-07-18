from flask import Flask
from app.db.db import db  
from app.routes.operation_routes import calc_bp
from app.routes.auth_routes import auth_bp
from app.routes.frontend_routes import frontend_bp

def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///math.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)
    app.register_blueprint(calc_bp, url_prefix="/api")
    app.register_blueprint(auth_bp, url_prefix="/auth")
    app.register_blueprint(frontend_bp)
    with app.app_context():
        from app.models.operation import Operation 
        db.create_all()

    return app
