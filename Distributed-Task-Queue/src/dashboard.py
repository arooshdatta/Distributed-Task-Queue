import os
import time

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_dashboard(workers, task_manager, logs):
    clear_screen()
    print("="*60)
    print(" DISTRIBUTED TASK QUEUE - MONITORING DASHBOARD")
    print("="*60)
    
    stats = task_manager.get_stats()
    
    # Top Stats Bar
    print(f" Pending: {stats['pending']} | Completed: {stats['completed']} | Failed (DLQ): {stats['failed']}")
    print("-" * 60)
    
    # Worker Status
    print(" WORKER STATUS")
    for w in workers:
        status = "IDLE"
        if w.current_task:
            status = f"BUSY -> {w.current_task.name} (P{w.current_task.priority})"
        print(f" [Worker-{w.worker_id}]: {status}")
        
    print("-" * 60)
    
    # Recent Logs
    print(" RECENT LOGS")
    for log in logs[-7:]: # Show last 7 logs
        print(f" > {log}")
        
    print("-" * 60)
    print(" Press Ctrl+C to stop simulation")