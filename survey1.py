import re

def main():
    fname = getFname()
    lname = getLname()
    dob = getDob()
    email = getEmail()
    zcode = getZcode()
    city = getCity()
    state = getState()
    race = getRace()
    age = getAge()
    sex = getSex()

    print(fname)
    print(lname)
    print(dob)
    print(email)
    print(zcode)
    print(city)
    print(state)
    print(race)
    print(age)
    print(sex)

def getFname():
    while True:
        x = input("Enter your first name:")
        if re.match("[a-zA-Z]+$", x):
            return x
        else:
            print("Please enter it again:")

def getLname():
    while True:
        x = input("Enter your last name:")
        if re.match("[a-zA-Z]+$", x):
            return x
        else:
            print("Please enter it again:")


def getDob():
    while True:
        x = input("Enter your date of birth (mm/dd/yy):")
        if re.match("[0-9/]+$", x):
            return x
        else:
            print("Please enter it again:")

def getEmail():
    while True:
        x = input("Enter your email:")
        if re.match("[a-zA-Z0-9@.]+$", x):
            return x
        else:
            print("Please enter it again:")


def getZcode():
    while True:
        x = input("Enter your zip code:")
        try:
            int(x)
            return x
        except ValueError:
            print("Please enter it again:")

def getCity():
    while True:
        x = input("Enter your city:")
        if re.match("[a-zA-Z]+$", x):
            return x
        else:
            print("Please enter it again:")

def getState():
    while True:
        x = input("Enter your state:")
        if re.match("[a-zA-Z]+$", x):
            return x
        else:
            print("Please enter it again:")

def getRace():
    while True:
        x = input("Enter your race:")
        if re.match("[a-zA-Z]+$", x):
            return x
        else:
            print("Please enter it again:")

def getAge():
    while True:
        x = input("Enter your age:")
        try:
            int(x)
            return x
        except ValueError:
            print("Please enter it again:")

def getSex():
    while True:
        x = input("Enter your sex:")
        if re.match("[a-zA-Z]+$", x):
            return x
        else:
            print("Please enter it again:")


main()
