import random, time
from multiprocessing import Pool 


def worker(name):
    """The work bit."""
    print(f"Started worker {name}")
    working_time = random.choice(range(1, 5))
    time.sleep(working_time)
    print(f"{name} worker finished in {working_time}.")


if __name__ == "__main__":
    processes = [f'computer_{i}' for i in range(15)]
    pool = Pool(processes=2)
    pool.map(worker, processes)
    pool.terminate()
