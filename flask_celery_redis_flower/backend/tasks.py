from celery import current_app

# Example task to add two numbers
@current_app.task
def add(x, y):
    return x + y

# Example task to simulate a long-running task (for testing purposes)
@current_app.task
def long_task():
    import time
    for i in range(10):
        print(f"Running step {i}...")
        time.sleep(1)  # Simulate a time-consuming task
    return "Task complete!"
