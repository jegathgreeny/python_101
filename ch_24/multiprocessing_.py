import random, time
import multiprocessing


def worker(name):
    """Outputs the working log."""
    print(f"Started worker {name}")
    working_time = random.choice(range(1, 5))
    time.sleep(working_time)
    print(f"{name} worker finished in {working_time}.")


if __name__ == "__main__":
    processes = []
    for i in range(5):
        process = multiprocessing.Process(target=worker, args=(f"computer_{i}",))
        processes.append(process)
        process.start()

    for proc in processes:
        proc.join()
