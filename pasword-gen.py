import random
import string

def strong():
    # length = 7
    a = ["!", "@", "#", "$"]
    characters = string.ascii_letters + string.digits
    random_string = ''.join(random.choice(characters) for _ in range(7))
    random_string += ''.join(random.choice(a) for _ in range(8))
    return random_string
strong()   

def week():
    length = 8
    characters = string.ascii_letters + string.digits
    random_string = ''.join(random.choice(characters) for _ in range(length))
    return random_string
week()
def medium():
    length = 10
    characters = string.ascii_letters + string.digits
    random_string = ''.join(random.choice(characters) for _ in range(length))
    return random_string
medium()



print("\nPassword Generator app")
def password():
    while True:
        num = input("Please Pick any one choice. (A,B,C,X)")
        if num == "A":
            print(week())
        elif num == "B":
            print(medium())
        elif num == "C":
            print(strong())
        elif num == "X":
            break
password()
