from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os

db = SQLAlchemy()

def create_app():
    load_dotenv()  # încarcă variabilele din .env
    print("Creating Flask application...")
    
    app = Flask(__name__)

    # Configurare DB din .env
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DB_URI', 'sqlite:///math.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    # Înregistrează rutele
    from app.routes.math_routes import math_bp
    app.register_blueprint(math_bp, url_prefix='/api')

    return app
