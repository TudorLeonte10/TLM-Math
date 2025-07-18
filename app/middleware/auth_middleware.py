import jwt
from flask import request, jsonify
from functools import wraps

SECRET_KEY = "supersecret" 

#de mutat in env daca facem cu docker

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization')

        if not token:
            return jsonify({'message': 'Token is missing'}), 401

        try:
            token = token.replace("Bearer ", "")
            payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
            request.user = payload['username']
        except jwt.ExpiredSignatureError:
            return jsonify({'message': 'Token expired'}), 403
        except jwt.InvalidTokenError:
            return jsonify({'message': 'Invalid token'}), 403

        return f(*args, **kwargs)
    return decorated

def requires_role(required_role):
    def wrapper(f):
        @wraps(f)
        def decorated(*args, **kwargs):
            token = request.headers.get('Authorization')
            if not token:
                return jsonify({'message': 'Token is missing'}), 401
            try:
                token = token.replace("Bearer ", "")
                payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
                request.user = payload['username']
                request.role = payload['role']
                if request.role != required_role:
                    return jsonify({'message': 'Access forbidden: insufficient privileges'}), 403
            except jwt.ExpiredSignatureError:
                return jsonify({'message': 'Token expired'}), 403
            except jwt.InvalidTokenError:
                return jsonify({'message': 'Invalid token'}), 403

            return f(*args, **kwargs)
        return decorated
    return wrapper
