import random, time

import threading


def worker(name):
    """An exmaple for multithreading."""
    print(f"Started worker {name}.")
    working_time = random.choice(range(1, 5))
    time.sleep(working_time)
    print(f"{name} worker finished in {working_time} seconds.")


if __name__ == "__main__":
    for i in range(5):
        thread = threading.Thread(
            target=worker,
            args=(f"computer_[i]",),
        )
        thread.start()
