from flask import Blueprint, render_template

frontend_bp = Blueprint('frontend_bp', __name__)

@frontend_bp.route('/')
def calculator_page():
    return render_template('calculator.html')
