# Write a program to create a dictionary that contains (i, i*i) such that i is an integral number between 1 and n (both included). 

# Take User Input of Number
n = int(input("Enter the value of n: "))
# Create a dictionary of squares
squares = {i : i*i for i in range(1, n+1)}
# Print the dictionary
print(squares)

