from flask import Blueprint, request, jsonify
import jwt
from datetime import datetime, timedelta

auth_bp = Blueprint('auth_bp', __name__)
SECRET_KEY = "supersecret" 

#trebuie mutat in env daca facem cu docker

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    if username == "admin" and password == "admin123":
        role = "admin"
    elif username == "user" and password == "user123":
        role = "user"
    else:
        return jsonify({"message": "Invalid credentials"}), 401

    token = jwt.encode({
        'username': username,
        'role': role,
        'exp': datetime.utcnow() + timedelta(hours=1)
    }, SECRET_KEY, algorithm="HS256")

    return jsonify({'token': token})