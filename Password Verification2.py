import re  
  
def validate_password(password):  
    if len(password) < 8:  
        return False  
    if not re.search("[a-z]", password):  
        return False  
    if not re.search("[A-Z]", password):  
        return False  
    if not re.search("[0-9]", password):  
        return False  
    return True  
  
password = "P@ssw0rd"  

if validate_password(password):  
    print("Valid password")  
else:  
    print("Invalid password")  