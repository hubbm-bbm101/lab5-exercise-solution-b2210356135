def checker(string):
    return ("@" in string and "." in string)
email = input("Your e-mail: ")

if (checker(email)):
    print("e-mail is valid")
else:
    print("e-mail is not valid")
    