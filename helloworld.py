print('Hello, World!')
key = ""
username = ""
username_login = ""
password_login = ""

def welcome():
    global username
    print("Welcome, " + username + "!")

def function():
    fuction = str(input("Please select fuction: (login/register)"))
    if fuction == "login":
        login()
    else:
        if fuction == "register":
            register()


def login():
    global key
    global username
    global username_login
    global password_login
    username_login = str(input("Please enter your username: "))
    password_login = str(input("Please enter your password: "))
    login2()


def login2():
    if (username_login == username and password_login == key):
        print("Login successful.")

    else:
        print("Login unsuccessful. Please try again.")
        function()


def register():
    global username
    global key
    username = str(input("Please enter your username: "))
    key = str(input("Please enter your password: "))
    welcome()
    function()

if username != "":
    welcome()
    function()
else:
    function()
