from flask import Flask
from app.db.db import db  

def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///math.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)

    with app.app_context():
        from app.models.operation import Operation 
        db.create_all()

    from app.routes.operation_routes import calc_bp
    app.register_blueprint(calc_bp, url_prefix="/api")

    return app
