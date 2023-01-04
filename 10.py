p=int(input("Enter the principle amount: "))
t=int(input("Enter the time(in years): "))
if p<200000 :
    r=10
elif p>=200000 and p<=1000000 :
   r=12
else:
   r=15
total= p*(1+r*t/100)
print("Your total amount of money is: %.2f" %total)
