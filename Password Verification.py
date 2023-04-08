import re

password = input("Enter string to test: ")

if re.fullmatch(r'[A-Za-z0-9@#$%^&+=]{8,}', password):
   print("Valid Password")
else:
    print("Not Valid Password")