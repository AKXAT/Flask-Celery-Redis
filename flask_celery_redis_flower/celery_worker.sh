#!/bin/bash

# Activate virtual environment if necessary
# source venv/bin/activate

# Start the Celery worker
celery -A backend worker --loglevel=info
