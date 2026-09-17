a = int(input("Enter your first side: "))
b = int(input("Enter your second side: "))
c = int(input("Enter your third side: "))
def check_triangle(a, b, c):
    if a**2 + b**2 == c**2:
        print("The triangle is a right triangle.")
    elif a**2 + c**2 == b**2:
        print("The triangle is a right triangle.")
    elif b**2 + c**2 == a**2:
        print("The triangle is a right triangle.")
    else:
        print("The triangle is not a right triangle.")

check_triangle(a, b, c)