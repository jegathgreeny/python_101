quote = "chaos is a ladder"

letter = "z"

for character in quote:
    if character == letter:
        print(f"found - {character}")
        break
    print(character)

else:
    print(f"{letter} not found.\n")


# To compare
letter = "d"

for character in quote:
    if character == letter:
        print(f"found - {character}")
        break
    print(character)

else:
    print(f"{letter} not found.")

""" A more proper way of communicating an error would be
 to raise an error an exception to signal
  the absence of a character than printing a message."""
