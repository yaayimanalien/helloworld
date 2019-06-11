print('Hello, World!')
key = True
username = True


def welcome():
    global username
    
    if username != True:
        fuction = str(input("Please select fuction: (login/register)"))
    if fuction == "login":
        login()
    else:
        if fuction == "register":
             register()
    # else:
        username = str(input("Please enter your username: "))
        welcome()
       
    else:
        print("Welcome, " + username + "!")
    

def login():
    global key
    password = str(input("Please enter your password: "))
    if password == key:
        print("Login successful.")
    else:
        print("Login unsuccessful. Please try again.")
        welcome()

def register():
    global username
    global key
    username = str(input("Please enter your username: "))
    key = str(input("Please enter your password: "))
    welcome()

welcome()
