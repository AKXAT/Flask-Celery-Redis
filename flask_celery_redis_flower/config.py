import os

# Flask configuration
SECRET_KEY = os.getenv('SECRET_KEY', 'mysecret')

# Redis and Celery configuration
BROKER_URL = os.getenv('BROKER_URL', 'redis://localhost:6379/0')
RESULT_BACKEND = os.getenv('RESULT_BACKEND', 'redis://localhost:6379/0')
