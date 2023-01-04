#Write a program to count the numbers of characters in a string and store them in a dictionary.

str=input("enter string : ")

f = {} 

for i in str: 

    if i in f: 

        f[i] += 1

    else: 

        f[i] = 1

print(f)