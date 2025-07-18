from flask import Blueprint
from app.controllers.operation_controller import (
    calculate_pow,
    calculate_fib,
    calculate_fact
)


from app.middleware.auth_middleware import token_required
#Adaugat pt autentificare

calc_bp = Blueprint('calc_bp', __name__)

@calc_bp.route("/calculate/pow", methods=["POST"])
#@token_required
def pow_calc():
    return calculate_pow()

@calc_bp.route("/calculate/fib", methods=["POST"])
#@token_required
def fib_calc():
    return calculate_fib()

@calc_bp.route("/calculate/fact", methods=["POST"])
#@token_required
def fact_calc():
    return calculate_fact()
