import redis
import json
from datetime import datetime

r = redis.Redis(host='localhost', port=6379, db=0)

def log_event(event, operation, input_data=None, result=None, error=None):
    message = {
        'event': event,
        'operation': operation,
        'input_data': input_data,
        'result': result,
        'error': error,
        'timestamp': datetime.utcnow().isoformat()
    } 
    r.publish('logs', json.dumps(message))

    