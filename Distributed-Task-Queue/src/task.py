import uuid
import time
from dataclasses import dataclass, field

@dataclass
class Task:
    priority: int  # Lower number = Higher priority
    name: str
    duration: int  # Simulation of how long the task takes (seconds)
    retries: int = 0
    max_retries: int = 3
    id: str = field(default_factory=lambda: str(uuid.uuid4())[:8])
    created_at: float = field(default_factory=time.time)

    def __lt__(self, other):
        # This allows the Min-Heap to compare tasks. 
        # If priorities are equal, the one created earlier goes first.
        if self.priority == other.priority:
            return self.created_at < other.created_at
        return self.priority < other.priority

    def __repr__(self):
        return f"[P{self.priority}] {self.name} (ID: {self.id})"