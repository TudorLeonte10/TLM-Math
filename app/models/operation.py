from app.db.db import db
from datetime import datetime

class Operation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    operation = db.Column(db.String(20), nullable=False)     
    input_data = db.Column(db.String(100), nullable=False)    
    result = db.Column(db.String(100), nullable=False)        
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
