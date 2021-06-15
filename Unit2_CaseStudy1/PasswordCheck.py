import string

retry = True
while retry:
    retry = False
    password = input("Enter password:")
    if len(password) > 12:
        print("Password length exceeds 12 characters. Retry..........!!!")
        retry = True
        continue
    if len(password) < 6:
        print("Password length is less than 6 characters. Retry..........!!!")
        retry = True
        continue
    if (len(set(password).intersection(set(['$','#','@'])))) <= 0:
        print("Password must include one special character $, #, @. Retry..........!!!")
        retry = True
        continue
    if (len(set(password).intersection(set(list(string.ascii_lowercase))))) <= 0:
        print("Password must include one lower case character. Retry..........!!!")
        retry = True
        continue
    if (len(set(password).intersection(set(list(string.ascii_uppercase))))) <= 0:
        print("Password must include one upper case character. Retry..........!!!")
        retry = True
        continue
    if (len(set(password).intersection(set(list(string.digits))))) <= 0:
        print("Password must include one digit. Retry..........!!!")
        retry = True
        continue
print("Password accepted!!!")
