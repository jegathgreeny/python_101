import random, time

from threading import Thread


class WritingThread(Thread):
    """A class to represent multiple threading."""

    def __init__(self, filename, no_of_lines, work_time=1):
        Thread.__init__(self)
        self.filename = filename
        self.no_of_lines = no_of_lines
        self.work_time = work_time

    def run(self):
        """Run the thread."""
        print(f"Writing {self.no_of_lines} lines of text to {self.filename}.")
        with open(self.filename, "w") as f:
            for line in range(self.no_of_lines):
                text = f"This is line {line+1}\n"
                f.write(text)
                time.sleep(self.work_time)
        print(f"Finished writing {self.filename}.")


if __name__ == "__main__":
    files = [f"test{x}.txt" for x in range(1, 6)]
    for filename in files:
        work_time = random.choice(range(1, 3))
        no_of_lines = random.choice(range(5, 20))
        thread = WritingThread(filename, no_of_lines, work_time)
        thread.start()
