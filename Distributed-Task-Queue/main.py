import time
import random
from src.task import Task
from src.queue_manager import TaskManager
from src.worker import Worker
from src.dashboard import print_dashboard

# Configuration
NUM_WORKERS = 3
TOTAL_TASKS = 20

def main():
    manager = TaskManager()
    logs = []

    def log_message(msg):
        timestamp = time.strftime("%H:%M:%S")
        logs.append(f"[{timestamp}] {msg}")

    # 1. Initialize Workers
    workers = []
    for i in range(NUM_WORKERS):
        w = Worker(worker_id=i+1, task_manager=manager, logger_func=log_message)
        w.start()
        workers.append(w)

    # 2. Simulate Adding Tasks dynamically
    task_names = ["Email_Blast", "Data_Process", "Image_Resize", "Report_Gen", "DB_Backup"]
    
    try:
        # Pre-fill some tasks
        for _ in range(5):
             priority = random.randint(1, 10) # 1 is highest, 10 is lowest
             t = Task(priority=priority, name=random.choice(task_names), duration=random.uniform(0.5, 2.0))
             manager.add_task(t)

        # Main Loop
        tasks_generated = 5
        while True:
            # Randomly add new tasks while running
            if tasks_generated < TOTAL_TASKS and random.random() > 0.7:
                priority = random.randint(1, 10)
                t = Task(priority=priority, name=random.choice(task_names), duration=random.uniform(0.5, 2.0))
                manager.add_task(t)
                log_message(f"NEW TASK ADDED: {t.name} (Priority {t.priority})")
                tasks_generated += 1

            # Update CLI Dashboard
            print_dashboard(workers, manager, logs)
            time.sleep(0.5)

            # Exit condition for demo
            stats = manager.get_stats()
            if stats['pending'] == 0 and all(w.current_task is None for w in workers) and tasks_generated >= TOTAL_TASKS:
                print_dashboard(workers, manager, logs)
                print("\nAll tasks processed! Exiting...")
                break

    except KeyboardInterrupt:
        print("\nStopping system...")

    # Cleanup
    for w in workers:
        w.stop()
    for w in workers:
        w.join()

if __name__ == "__main__":
    main()