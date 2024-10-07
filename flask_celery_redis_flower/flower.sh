#!/bin/bash

# Start Flower for monitoring Celery
celery -A backend flower --port=5001
