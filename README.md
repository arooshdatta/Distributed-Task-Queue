# 🚀 Distributed Task Queue System

> A robust, multi-threaded task scheduling system implemented in Python with priority handling and real-time monitoring.

## 📖 Overview
This project simulates a backend system managing background jobs across multiple workers. Unlike standard First-In-First-Out (FIFO) queues, this system uses a **Priority Queue (Min-Heap)** to ensure high-priority tasks are processed first. It features a real-time CLI dashboard, fault tolerance with retry logic, and a Dead Letter Queue (DLQ) for failed jobs.

## 🌟 Key Features
- **Priority Scheduling:** Uses `heapq` to process high-priority tasks (e.g., P1) before lower ones (e.g., P10).
- **Concurrent Workers:** Simulates a distributed environment using Python `threading`.
- **Fault Tolerance:** Automatic retry mechanism (up to 3 times) for tasks that fail due to simulated network errors.
- **Dead Letter Queue (DLQ):** Captures tasks that fail max retries for later inspection/debugging.
- **Real-time Dashboard:** A live, refreshing CLI interface monitoring worker status and queue depth.

## 🛠️ Tech Stack
- **Language:** Python 3.8+
- **Core Concepts:** Min-Heap, Threading (Concurrency), Locks (Mutex), Queue
- **Architecture:** Producer-Consumer Pattern

## 📂 Project Structure
```text
distributed-task-queue/
│
├── src/
│   ├── __init__.py      # Package initializer
│   ├── task.py          # Task data class with comparison logic
│   ├── queue_manager.py # Heap management and DLQ logic
│   ├── worker.py        # Worker thread implementation
│   └── dashboard.py     # CLI Visualization
│
├── main.py              # Entry point / Simulation orchestrator
├── requirements.txt     # Dependencies
└── README.md            # Documentation
```

## ⚡ How It Works
1. **Task Submission:** Tasks are assigned a priority (1-10) and pushed into a `heapq`.
2. **Worker Selection:** Workers act as consumers, pulling the highest priority task available.
3. **Execution & Failure:** - If a task succeeds, it is marked complete.
   - If it fails (simulated random failure), it retries up to 3 times.
   - If it still fails, it is moved to the **Dead Letter Queue**.

## 🚀 Getting Started

### Prerequisites
- Python 3.x installed

### Running the System
Clone the repository and run the main script:

```bash
python main.py
