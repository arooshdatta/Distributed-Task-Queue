import heapq
import threading

class TaskManager:
    def __init__(self):
        self.task_heap = []  # The Min-Heap
        self.lock = threading.Lock() # Thread safety is crucial here
        self.dead_letter_queue = [] # For tasks that failed max_retries
        self.completed_tasks = 0
        self.failed_tasks = 0

    def add_task(self, task):
        with self.lock:
            heapq.heappush(self.task_heap, task)

    def get_next_task(self):
        with self.lock:
            if self.task_heap:
                return heapq.heappop(self.task_heap)
            return None

    def add_to_dead_letter(self, task, reason="Max retries reached"):
        with self.lock:
            self.dead_letter_queue.append((task, reason))
            self.failed_tasks += 1

    def mark_completed(self):
        with self.lock:
            self.completed_tasks += 1

    def get_stats(self):
        with self.lock:
            return {
                "pending": len(self.task_heap),
                "completed": self.completed_tasks,
                "failed": len(self.dead_letter_queue),
                "dlq_items": [t[0].name for t in self.dead_letter_queue[-5:]] # Show last 5 failed
            }