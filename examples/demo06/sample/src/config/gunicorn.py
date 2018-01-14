# gunicorn -c config/gunicorn.py --worker-class sanic.worker.GunicornWorker server:app
bind = '127.0.0.1:8001'
backlog = 2048

workers = 2
worker_connections = 1000
timeout = 30
keepalive = 2

spew = False
daemon = False
umask = 0
