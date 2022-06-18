print("What is your Age (input age value only)")
Age = int(input())
if Age <= 12:
    print("You are not a teenager yet")
elif 13 <= Age <= 19:
    print("You are a teenager")
elif 20 <= Age <= 30:
    print("You are a Young adult") 
elif 31<= Age <= 50:
    print("You are an adult")
else:
    Age >= 51
    print("You are and Old man")
    print("Thank you sir")

#Even and odd number
print("Input any integer value")
Value = int(input())
if Value % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")