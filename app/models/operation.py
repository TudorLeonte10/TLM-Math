from app.db.db import db
from datetime import datetime

class Operation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    operation = db.Column(db.String(20), nullable=False)     
    input_data = db.Column(db.String(100), nullable=False)    
    result = db.Column(db.String(100), nullable=False)        
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False)
    password = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    role = db.Column(db.String(20), default='user')  # Default role is 'user'
