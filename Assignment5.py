import re

pan = input("Enter your PAN number: ")

pattern = r'^[A-Z]{5}[0-9]{4}[A-Z]{1}$'

if re.match(pattern, pan):
    print("Valid PAN number.")
else:
    print("Invalid PAN number.")