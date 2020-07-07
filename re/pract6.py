import re

def checkEmail(email):
    result = re.search(r'^[\w.]+@[\w.]+\.\w{2,}$',email)
    if result is not None:
        return True
    else:
        return False

def checkPhone(phone):
    res = re.search(r'^(\+7\-?|8\-?|7\-?)?\ ?(\(\d{3}\)|\d{3}|\d{3}\-)\ ?\d{3}[ -]?\d{2}[ -]?\d{2}$',phone)
    if res is not None:
        return True
    else:
        return False

def check_string(inputString):
    if inputString.find('@') != -1:
        return checkEmail(inputString)
    else:
        return checkPhone(inputString)

print(check_string(input()))