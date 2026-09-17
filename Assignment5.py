import re

pan = input("Enter your PAN number: ")
if re.match(r'^[A-Z]{5}[0-9]{4}[A-Z]{1}$', pan):
    print("Valid PAN number.")
else:
    print("Invalid PAN number.")