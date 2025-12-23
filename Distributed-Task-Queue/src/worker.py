import threading
import time
import random

class Worker(threading.Thread):
    def __init__(self, worker_id, task_manager, logger_func):
        super().__init__()
        self.worker_id = worker_id
        self.task_manager = task_manager
        self.logger = logger_func # Callback to update the dashboard
        self.running = True
        self.current_task = None

    def run(self):
        while self.running:
            task = self.task_manager.get_next_task()
            
            if task:
                self.current_task = task
                self.process_task(task)
                self.current_task = None
            else:
                # Sleep briefly to prevent CPU spinning if queue is empty
                time.sleep(0.5)

    def process_task(self, task):
        try:
            self.logger(f"Worker-{self.worker_id} started {task}")
            
            # Simulate work
            time.sleep(task.duration)
            
            # Simulate random failure (10% chance)
            if random.random() < 0.1: 
                raise Exception("Random Network Error")

            self.task_manager.mark_completed()
            self.logger(f"Worker-{self.worker_id} finished {task}")

        except Exception as e:
            self.logger(f"Worker-{self.worker_id} FAILED {task}: {e}")
            
            if task.retries < task.max_retries:
                task.retries += 1
                self.logger(f"Retrying task {task.id} ({task.retries}/{task.max_retries})")
                self.task_manager.add_task(task) # Re-queue
            else:
                self.logger(f"Moving {task.id} to Dead Letter Queue")
                self.task_manager.add_to_dead_letter(task)

    def stop(self):
        self.running = False