import redis
import json

r = redis.Redis(host='localhost', port=6379, db=0)
p = r.pubsub()
p.subscribe('logs')

print("Listening for log messages...")
for messages in p.listen():
    if messages['type'] == 'message':
        log = json.loads(messages['data'])
        print(f"[{log['timestamp']}] {log['event'].upper()} - {log['operation']}: {log.get('input')} → {log.get('result') or log.get('error')}")