from flask import Blueprint
from app.controllers.operation_controller import (
    calculate_pow,
    calculate_fib,
    calculate_fact
)

calc_bp = Blueprint('calc_bp', __name__)

@calc_bp.route("/calculate/pow", methods=["POST"])
def pow_calc():
    return calculate_pow()

@calc_bp.route("/calculate/fib", methods=["POST"])
def fib_calc():
    return calculate_fib()

@calc_bp.route("/calculate/fact", methods=["POST"])
def fact_calc():
    return calculate_fact()
