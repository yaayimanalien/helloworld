print('Hello, World!')
key = ("hello123")
name = True
username = True


def welcome():
    global name
    if name != True:
        print("Welcome, " + name + "!")
        fuction = str(input("Please select fuction: (login/register)"))
        if fuction == "login":
            login()
        else:
            if fuction == "register":
                register()
    else:
        name = str(input("Please enter your name: "))
        welcome()


def login():
    global key
    password = str(input("Please enter your password: "))
    if password == key:
        print("Login successful.")
    else:
        print("Login unsuccessful. Please try again.")
        login()

def register():
    global username
    global key
    username = str(input("Please enter your username: "))
    key = str(input("Please enter your password: "))
    welcome()

welcome()
