import redis
import json
import os

r = redis.Redis(host='localhost', port=6379, db=0)
p = r.pubsub()
p.subscribe('logs')

log_folder = 'app/logging/'
os.makedirs(log_folder, exist_ok=True)
log_file = os.path.join(log_folder, 'app.log')

print("Listening for log messages...")
with open(log_file, 'a', encoding='utf-8') as f:
    for messages in p.listen():
        if messages['type'] == 'message':
            log = json.loads(messages['data'])
            print(f"[{log['timestamp']}] {log['event'].upper()} - {log['operation']}: {log['input_data']} → {log.get('result') or log.get('error')}")
            line = (f"[{log['timestamp']}] {log['event'].upper()} - {log['operation']}: {log['input_data']} → {log.get('result') or log.get('error')}\n")
            f.write(line)
            f.flush()