print("Welcome to LINAR staff exprience")
print("This program calculates your salary based on your exprience")
print ("input your years of exprience")
Salary = 20000
Experience = int(input())
if 0 <= Experience <= 2:
    print("You are in level one")
    print("Your payment is;", str(Salary))
elif 3 <= Experience <= 5:
    print("You are in level Two")
    print("Your payment is;",int(Salary * 1.25))
elif 6 <= Experience <= 8:
    print("You are in level Three")
    print("Your payment is;",int(Salary * 1.25**2))
elif 9 <= Experience <= 11:
    print("You are in level Four")
    print("Your payment is;",int(Salary * 1.25**3))
elif 12 <= Experience <= 14:
    print("You are in level Five")
    print("Your payment is;",int(Salary * 1.25**4))
elif 15 <= Experience <= 17:
    print("You are in level Six")
    print("Your payment is;",int(Salary * 1.25**5))
elif 18 <= Experience <= 20:
    print("You are in level Seven")
    print("Your payment is;",int(Salary * 1.25**6))
elif 21 <= Experience <= 23:
    print("You are in level Eight")
    print("Your payment is;",int(Salary * 1.25**7))
elif 24 <= Experience <= 26:
    print("You are in level Nine")
    print("Your payment is;",int(Salary * 1.25**8))
elif 27 <= Experience <= 29:
    print("You are in level Ten")
    print("Your payment is;",int(Salary * 1.25**9))
elif 30 <= Experience <= 32:
    print("You are in level Eleven")
    print("Your payment is;",int(Salary * 1.25**10))
else:
    print("Opps")
    print("Eleven is the Maximum level")