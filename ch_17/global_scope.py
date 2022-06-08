def add():
    # The global statement gives the variable a global scope.
    global b
    a = 2
    b = 4
    return a + b

def subtract():
    a = 3
    # Returns only the local scope varaibles and other stuff.
    print(locals())
    # Returns only the global scope variables and other stuff.
    print(globals())
    return a - b

print(add())
print(subtract())