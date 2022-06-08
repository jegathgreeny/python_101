matrix = [[1, 2, 4], [8, 3, 7], [9, 0, 6]]

# The outer loop is inside the first square bracket.
# The nested loop is inside the second square bracket. 
double = [[element * 2 for element in row] for row in matrix]
print(double)