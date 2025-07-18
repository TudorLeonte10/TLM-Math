from app.logging.redis_logger import log_event

log_event('server_error', 'pow', 'base=2, exp=2', 'all good')