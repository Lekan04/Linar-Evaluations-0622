# Using the If, Elif and Else Statement, write a code that group users into group A B and C
# If user is single let user know he or she falls in group A
# If user is in a relationship let user know he or she falls in group B
# if user is married let user know he or she falls under group C
print("Hello user, What is your marital status? (Single, Married, Dating)")
Status = str(input())
if Status == "Single":
    print("Dear user, you fall under Group A")
    print("Thank you for using this service.")
elif Status == "Dating":
    print("Dear user, you fall under Group B")
    print("Thank you for using this service.")
else:
    Status == "Married"
    print("Dear user, you fall under Group C")
    print("Thank you for using this service.")

print("Welcome to LINAR staff exprience")
print("This program calculates your salary based on your exprience")
print ("input your years of exprience")
Salary = 20000
Exprience = int(input())
if 0 <= Exprience <= 2:
    print("You are in level one")
    print("Your payment is;", str(Salary))
elif 3 <= Exprience <= 5:
    print("You are in level Two")
    print("Your payment is;",int(Salary * 1.25))
elif 6 <= Exprience <= 8:
    print("You are in level Three")
    print("Your payment is;",int(Salary * 1.25**2))
