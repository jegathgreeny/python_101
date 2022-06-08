def func_info(arg1, arg2):
    print('Decorator arg1 = ' + str(arg1))
    print('Decorator arg2 = ' + str(arg2))

    def the_real_decorator(function):
        def wrapper(*args, **kwargs):
            print(f'Function {function.__name__} args: {str(args)} kwargs: {str(kwargs)}')
            return function(*args, **kwargs)
        return wrapper
    return the_real_decorator

@func_info(3, 'Python')
def treble(number):
    return number * 3

print(treble(5))