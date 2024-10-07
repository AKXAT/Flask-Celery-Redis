from flask import Flask
from celery import Celery
import os

def make_celery(app):
    celery = Celery(
        app.import_name,
        backend=app.config['RESULT_BACKEND'],
        broker=app.config['BROKER_URL']
    )
    celery.conf.update(app.config)
    return celery

def create_app():
    app = Flask(__name__)
    
    # Set configuration for Redis
    app.config['BROKER_URL'] = 'redis://127.0.0.1:6379/0'
    app.config['RESULT_BACKEND'] = 'redis://127.0.0.1:6379/0'

    # Initialize Celery with the Flask app context
    celery = make_celery(app)

    # Register the blueprint
    from .views import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app

# Create a Celery instance globally to be accessed from tasks
celery = make_celery(create_app())