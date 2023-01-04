#Write a program to create a dictionary by combining two lists ‘name’ for employee name and ‘salary’ for employee salary. Use the list ‘name’ as the key and ‘salary’ as the value of dictionary elements.

names = ["Reetika","Surbhi","Aman","Pogo","Rohan"]
salaries =[5000,8500,5000,4800,10000]
dict = {}
i = 0
for name in names:
    dict[name] = salaries[i]
    i = i+1
print(dict)