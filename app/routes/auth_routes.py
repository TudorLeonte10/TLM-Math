from flask import Blueprint, request, jsonify
import jwt
from datetime import datetime, timedelta
from app.models.operation import Users
from app.logging.redis_logger import log_event

auth_bp = Blueprint('auth_bp', __name__)
SECRET_KEY = "supersecret" 



@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    user = Users.query.filter_by(username=username).first()

    if not user or user.password != password:
        log_event('login_error', 'auth', f'username={username}', error='Invalid credentials')
        return jsonify({"message": "Invalid credentials"}), 401

    token = jwt.encode({
        'username': user.username,
        'role': user.role,
        'exp': datetime.utcnow() + timedelta(hours=1)
    }, SECRET_KEY, algorithm="HS256")

    log_event('login_success', 'auth', f'username={username}', result='Login successful')
    return jsonify({'token': token})