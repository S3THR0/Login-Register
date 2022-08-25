import sqlite3
import maskpass
import socket


conn = sqlite3.connect("projectx.db")
#sqlite3.connect(":memory:") for temp
#create cursor
c = conn.cursor()

def Roster():
    #connect to database
    conn = sqlite3.connect("projectx.db")
    #sqlite3.connect(":memory:") for temp
    # #create cursor
    c = conn.cursor()
    #query database
    c.execute("SELECT * FROM members")
    # #print(c.fetchone()[3])
    # #print(c.fetchmany())
    # #print(c.fetchall())
    #organized fetch
    datas = c.fetchall()
    print("NAME " + "\t\t\tUSERNAME " + "\tEMAIL")
    print("---------" + "\t\t---------" + "\t--------")
    for data in datas:
        print(data[0] + " " + data[1] + "\t\t" + data[3] + "\t\t" + data[2] )
    #commit command/save our progress
    conn.commit()
    # #close connection
    conn.close()


def Credentials():
    print("Credential Check")
    #connect to database
    conn = sqlite3.connect("projectx.db")
            #sqlite3.connect(":memory:") for temp
    #create cursor
    c = conn.cursor()
    statement = "SELECT user_name, password FROM members"
    c.execute(statement)
    #organized fetch
    datas = c.fetchall()
    print("USERNAME " + "\tPASSWORD")
    print("---------" + "\t--------")
    for data in datas:
            print(data[0] + "\t\t" + data[1])


    k=input("press enter to exit")
    #commit command/save our progress
    conn.commit()
    #close connection
    conn.close()

def Register():
    #connect to database
    conn = sqlite3.connect("projectx.db")
            #sqlite3.connect(":memory:") for temp
    #create cursor
    c = conn.cursor()

    firstname = input("What is your first name?:")
    lastname = input("What is your last name?:")
    email = input("What is your email?:")
    emailconfirm = input("Confirm your email:")

    if (email == emailconfirm):
        username = input("Create Username:")
        if username == "root":
            privilege = 1
        else:
            privilege = 0

        password = maskpass.askpass(mask="")
        member_info = [
                        (firstname, lastname, email, username, password, privilege)
                    ]

        c.executemany("INSERT INTO members VALUES (?,?,?,?,?,?)", member_info)
        print("Successfully Registered " + username)
        #commit command/save our progress
        conn.commit()
        # #close connection
        conn.close()
    else:
        print("Please review email!!")


def RRegister():
    #connect to database
    conn = sqlite3.connect("projectx.db")
            #sqlite3.connect(":memory:") for temp
    #create cursor
    c = conn.cursor()

    firstname = input("What is your first name?:")
    lastname = input("What is your last name?:")
    email = input("What is your email?:")
    emailconfirm = input("Confirm your email:")

    if (email == emailconfirm):
        username = input("Create Username:")
        if username == "root":
            privilege = 1
        else:
            privilege = 0

        password = maskpass.askpass(mask="")
        print("0 = non root, 1 = root")
        priveledge =input("Priveledge (0 or 1)")
        member_info = [
                        (firstname, lastname, email, username, password, privilege)
                    ]

        c.executemany("INSERT INTO members VALUES (?,?,?,?,?,?)", member_info)
        print("Successfully Registered " + username)
        #commit command/save our progress
        conn.commit()
        # #close connection
        conn.close()
    else:
        print("Please review email!!")

def Login():
    username = input("Username:")
    password = maskpass.askpass(mask="")
    hostname = socket.gethostname()
    IPAddr = socket.gethostbyname(hostname)

    #connect to database
    conn = sqlite3.connect("projectx.db")
            #sqlite3.connect(":memory:") for temp
    #create cursor
    c = conn.cursor()

    statement = f"SELECT user_name from members WHERE user_name = '{username}' AND password = '{password}';"
    c.execute(statement)
    if not c.fetchone():  # An empty result evaluates to False.
        print("Login failed")
        exit()
    else:
        print("Welcome " + username)
        print("Your Computer Name is: " + hostname)
        print("Your Computer local IP Address is: " + IPAddr)

    RPcheck = f"SELECT user_name FROM members WHERE user_name = '{username}' AND privilege = '1'"
    c.execute(RPcheck)
    if not c.fetchone():
        print("You are not admin")
        exit()
    else:
        pass

    menu = {}
    menu['1']="Roster" 
    menu['2']="Credentials"
    menu['3']="Register User"
    menu['7']="Exit"
    while True:
        options = menu.keys()
        for entry in options:
            print(entry, menu[entry])
        
        selection = input("Please Select:")
        if selection =='1': 
            Roster()
        elif selection == '2':
            Credentials()
        elif selection == '3':
            RRegister()
        elif selection == '7':
            os.system("clear")
            break
        else:
            print("Unknown Option Selected!")
    #commit command/save our progress
    conn.commit()
    # #close connection
    conn.close()





#commit command/save our progress
    conn.commit()
    # #close connection
    conn.close()
