a = int(input("Enter your first number: "))
b = int(input("Enter your second number: "))
c = int(input("Enter your third number: "))
if a > b and a > c:
    print("The largest number is:", a)
elif b > a and b > c:
    print("The largest number is:", b)  
else:
    print("The largest number is:", c)