from flask import Blueprint, render_template

frontend_bp = Blueprint('frontend_bp', __name__)

@frontend_bp.route('/calculator')
def calculator_page():
    return render_template('calculator.html')

@frontend_bp.route('/login')
def login_page():
    return render_template('login.html')