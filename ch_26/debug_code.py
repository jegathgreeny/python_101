def log(num):
    """Prints out the number and adds 2 to it."""
    print(f"Processing {num}")
    print(f"Adding: {num + 2}")

def looper(num):
    """Calls the log function for n number of times."""
    for i in range(num):
        # This is a built-in debugging tool.
        # Most IDE will recognize them as well.
        breakpoint()
        log(i)

looper(10)