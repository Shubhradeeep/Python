''' Write a program that prompts users to enter numbera.This process repeats until the user enters -1. Finally the
 program prints the count of prime and composite numbers entered'''

p = []
c = []
while 1:
    a = int(input('Enter a number> '))
    if a != -1:
        x = 2
        ch = 0
        if a <= 1:
            ch = 1
        while x <= a**0.5:
            if a % x == 0:
                ch = 1
                break
            else:
                x += 1
        if ch == 0:
            p.append(a)
        else:
            c.append(a)
    else:
        print('\nNumbers you Entered-\nPrime Numbers-',
              p, '\nComposite Numbers-', c)
