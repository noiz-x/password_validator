#!/usr/bin/env python
# coding: utf-8

# In[7]:


#import
import string

#reasons for the password being invalid
reasons = ["eight characters","one uppercase letter","one lowercase letter","one digit","one of the four special characters \"@ ! # $\""]

#ask for user input
password = input("Enter your password: ")

# --FUNCTIONS------------------------
def length_test(password):
    if len(password) >= 8:
        return True
    else:
        return False
        
def uppercase_test(password):
    for i in password:
        if i in string.ascii_uppercase:
            return True
            break
        else:
            continue
    return False
            
def lowercase_test(password):
    for i in password:
        if i in string.ascii_lowercase:
            return True
            break
        else:
            continue
    return False
            
def digit_test(password):
    for i in password:
        if i in string.digits:
            return True
            break
        else:
            continue
    return False
          
def special_character_test(password):
    for i in password:
        if i in "!@#$":
            return True
            break
        else:
            continue
    return False
            
# ASSIGNMENT OF FUNCTION VALUES            
a = length_test(password)
b = uppercase_test(password)
f = lowercase_test(password)
d = digit_test(password)
e = special_character_test(password)

# printing of validity
if  length_test(password) == True and b == True and f == True and d == True and e == True:
    print("Valid!")
else:
    print("Invalid!")

# printing of reasons
c = 1
if a == False:
    v = print(f"Reason{c}: your password should contain at least {reasons[0]}.")
    c += 1
if b == False:
    v = print(f"Reason{c}: your password should contain at least {reasons[1]}.")
    c += 1
if f == False:
    v = print(f"Reason{c}: your password should contain at least {reasons[2]}.")
    c += 1
if d == False:
    v = print(f"Reason{c}: your password should contain at least {reasons[3]}.")
    c += 1
if e == False:
    v = print(f"Reason{c}: your password should contain at least {reasons[4]}.")
    c += 1


# In[ ]:




