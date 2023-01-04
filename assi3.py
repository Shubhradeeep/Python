# swapping using the third variable
a=float(input("Enter the first number"))
b=float(input("Enter the second number"))
c=a
a=b
b=c
print("the swapped numbers using the third variable are",a,b)


# swapping without third variable
a=float(input("Enter the first number"))
b=float(input("Enter the second number"))

a=a+b
b=a-b
a=a-b
print("\nThe swapped numbers without using the third varible are",a,b)