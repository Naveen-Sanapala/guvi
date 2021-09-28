def register():
    users = open("users.txt", "r")
    users_indb = []
    passwords_list = []
    for i in users:
        a, b = i.split(" ")
        users_indb.append(a.strip())
        passwords_list.append(b.strip())
    user_dict = dict(zip(users_indb, passwords_list))

    username = input("enter username/EmailId: ")
    if username in user_dict:
        print("Username already exists,try another username or login with existing username")
        home_screen()
    elif not username[0].isalpha() or "@" not in username or "." not in username or "@." in username:
        print("invalid username")
        register()

    def set_password():

        password = input("enter password: ")
        reenter_password = input("re-enter password: ")
        if password != reenter_password:
            print("Password not matching")
            set_password()
        else:
            import re
            flag = 0
            while True:
                if (len(password)) < 5 or len(password) > 16:
                    flag = -1
                    break
                elif not re.search("[a-z]", password) or not re.search("[A-Z]", password):
                    flag = -1
                    break
                elif not re.search("[0-9]",password):
                    flag = -1
                    break
                elif not re.search("[!@#$%^&*()_+]", password):
                    flag = -1
                    break
                else:
                    flag = 0
                    users = open("users.txt", "a")
                    users.write(username + " " + password + "\n")
                    print("Registration Successful")
                    home_screen()
                    break
            if flag == -1:
                print("password not valid")
                set_password()

    set_password()


def forgot_password():
    users = open("users.txt", "r")
    users_indb = []
    passwords_list = []
    for i in users:
        a, b = i.split(" ")
        users_indb.append(a.strip())
        passwords_list.append(b.strip())
    user_dict = dict(zip(users_indb, passwords_list))
    u_name = input("Enter your username/EmailId:")
    if u_name in user_dict:
        print(user_dict[u_name])
    else:
        print("user name does not exists, register")
        register()


def login():
    user_n = input("enter username/EmailId:")
    user_password = input("Enter password:")
    users = open("users.txt", "r")
    users_indb = []
    passwords_list = []
    for i in users:
        a, b = i.split(" ")
        users_indb.append(a.strip())
        passwords_list.append(b.strip())
    user_dict = dict(zip(users_indb, passwords_list))
    if user_n in user_dict:
        if user_password == user_dict[user_n]:
            print("Login successful")
        else:
            print("passoword Incorrect")
            print("forgot password?")
            fp=input("Y/N?")
            if  fp=="Y":
                forgot_password()
            elif fp=="N":
                login()
            else:
                print("invalid choice, Please choose Y or N")
    else:
        print("username not found")
        print("Please Register")
        register()


def home_screen():
    print("1. Resister\n2. Login")
    n = input("choose 1 or 2:")
    if int(n) == 1:
        register()
    elif int(n) == 2:
        login()

    else:
        print("please choose either 1 or 2")
        home_screen()


a = home_screen()