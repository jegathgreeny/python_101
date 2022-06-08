# To output selected text.
# The number represents the position.
# Starting at 0.
with open("example.txt") as file:
    file.seek(5)
    chunk = file.read()
    print(chunk)
    file.seek(0)
    chunk = file.read()
    print(chunk)