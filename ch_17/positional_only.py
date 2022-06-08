def positional(name, age, /, a, b, *, key):
    """Allows only positional and keyword arguments."""
    print(name, age, a, b, key)

positional('Mark', 17, 2, b=4, keyword='test')