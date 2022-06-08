import random, time

import threading


class WorkerThread(threading.Thread):
    """A class to represent multiple threading."""

    def __init__(self, name):
        """Initialize attributes."""
        threading.Thread.__init__(self)
        self.name = name
        self.id = id(self)

    def run(self):
        """Run the thread."""
        worker(self.name, self.id)


def worker(name, instance_id):
    """Does the threading."""
    print(f"Started worker {name} - {instance_id}")
    working_time = random.choice(range(1, 5))
    time.sleep(working_time)
    print(f"{name} - {instance_id} worker finished in {working_time} seconds.")


if __name__ == "__main__":
    for i in range(5):
        thread = WorkerThread(f"computer_{i}")
        thread.start()
