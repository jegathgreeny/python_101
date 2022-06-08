def func_info(func):
    def wrapper(*args):
        print(f"Function name: {func.__name__}")
        print(f"Function docstring: {str(func.__doc__)}")
        result = func(*args)
        return result
    return wrapper

@func_info
def triple(a):
    """A function that triples it's input."""
    return a * 3

@func_info
def double(a):
    """A function that doubles it's input."""
    return a * 2

# new_treple = wrapper(treple, 5)
# print(new_treple)

print(double(5))
print(triple(10))