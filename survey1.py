import re

def main():
    fname = input(str("Enter your first name:"))
    lname = input(str("Enter your last name:"))
    dob = getDob()
    email = input(str("Enter your email:"))
    zcode = getZcode()
    city = input(str("Enter your city:"))
    state = input(str("Enter your state:"))
    race = input(str("Enter your race:"))
    age = getAge()
    sex = input(str("Enter your sex:"))

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

def getDob():
    while True:
        x = input("Enter your date of birth (mm/dd/yy):")
        if re.match("[0-9/]+$", x):
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

def getAge():
    while True:
        x = input("Enter your zip age:")
        try:
            int(x)
            return x
        except ValueError:
            print("Please enter it again:")



main()