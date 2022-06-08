def bold(func):
    print(f"You are wrapping {func.__name__} in bold.")
    def wrapper():
        return "<b>" + func() + "</b>"
    return wrapper

def italic(func):
    print(f"You are wrapping {func.__name__} in italic.")
    def wrapper():
        return "<i>" + func() + "</i>"
    return wrapper

@bold
@italic
def format_text():
    return 'Chaos is a ladder'

print(format_text())