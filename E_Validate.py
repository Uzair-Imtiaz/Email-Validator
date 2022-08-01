import re
def emailValidate():
    regex = r'\b[A-Za-z0-9._]+@[A-Za-z0-9]+\.[A-Z|a-z]{2,3}\b'
    email = input('enter: ')
    return (re.fullmatch(regex,email))
