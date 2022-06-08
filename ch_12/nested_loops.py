currently_watching = [
    ["Seinfield", "The boys"],
    ["kill bill", "awakenings"],
    ["python 101", "crime and punishment"],
]

# The outer loop will extract each list.
for watching in currently_watching:
    print(watching)
    # The inner loop extracts each item within the nested list.
    for nested in watching:
        print(nested)

# This type of code is useful when the nested lists are of varying lengths.
