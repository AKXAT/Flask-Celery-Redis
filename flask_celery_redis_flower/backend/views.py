from flask import Blueprint, jsonify, request
from .tasks import add, long_task

# Create a blueprint for routes
main = Blueprint('main', __name__)

# Route to trigger the 'add' task
@main.route('/add', methods=['POST'])
def add_numbers():
    data = request.get_json()
    x = data.get('x')
    y = data.get('y')

    # Send the task to Celery
    task = add.apply_async(args=[x, y])

    return jsonify({
        'task_id': task.id,
        'status': 'Task submitted!',
    }), 202

# Route to trigger the 'long_task' (for testing)
@main.route('/longtask', methods=['GET'])
def start_long_task():
    task = long_task.apply_async()

    return jsonify({
        'task_id': task.id,
        'status': 'Long task submitted!',
    }), 202

# Route to check task status
@main.route('/status/<task_id>', methods=['GET'])
def task_status(task_id):
    task = add.AsyncResult(task_id)

    if task.state == 'PENDING':
        response = {
            'state': task.state,
            'status': 'Pending...',
        }
    elif task.state == 'SUCCESS':
        response = {
            'state': task.state,
            'result': task.result,
        }
    else:
        response = {
            'state': task.state,
            'status': str(task.info),  # Can contain error messages or other info
        }

    return jsonify(response)
