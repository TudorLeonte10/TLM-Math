from flask import Blueprint, request, jsonify
import jwt
from datetime import datetime, timedelta
from app.models.operation import Users

auth_bp = Blueprint('auth_bp', __name__)
SECRET_KEY = "supersecret" 
#trebuie mutat in env daca facem cu docker


@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    user = Users.query.filter_by(username=username).first()

    if not user or user.password != password:
        return jsonify({"message": "Invalid credentials"}), 401

    token = jwt.encode({
        'username': user.username,
        'role': user.role,
        'exp': datetime.utcnow() + timedelta(hours=1)
    }, SECRET_KEY, algorithm="HS256")

    return jsonify({'token': token})