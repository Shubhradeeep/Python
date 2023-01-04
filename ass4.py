a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

#swapping using bitwise operators
a = a ^ b
b = a ^ b
a = a ^ b

#printing the output
print("Swapped value of x is %d & y is %d" %(a,b))