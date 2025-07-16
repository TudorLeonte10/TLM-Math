from flask import Blueprint, request, jsonify
from app.controllers.math_controller import calculate_pow

math_bp = Blueprint('math_bp', __name__)

@math_bp.route('/pow', methods=['GET'])
def pow_route():
    try:
        base = request.args.get('base', type=float)
        exp = request.args.get('exp', type=float)

        if base is None or exp is None:
            return jsonify({'error': 'Missing parameters base or exp'}), 400

        result = calculate_pow(base, exp)
        return jsonify({'result': result})
    except Exception as e:
        return jsonify({'error': str(e)}), 500
