# Comprehensions automatically appends the values.
odd = [x for x in range(10) if x % 2 != 0]

print(odd)

# Converts a dictionary into a list nested with tuples.
dictionary = {1: "dog", 2: "fish", 3: "hen"}
list_tuple = [(num, animal) for num, animal in dictionary.items() if dictionary[num] == animal]

print(list_tuple)