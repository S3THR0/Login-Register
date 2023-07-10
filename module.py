import sqlite3
import maskpass
import socket

DATABASE = "projectx.db"

def connect_to_db():
    return sqlite3.connect(DATABASE)

def disconnect_from_db(conn):
    conn.commit()
    conn.close()

def Roster(conn):
    c = conn.cursor()
    c.execute("SELECT * FROM members")
    datas = c.fetchall()
    print("NAME \t\t\tUSERNAME \tEMAIL")
    print("---------\t\t---------\t--------")
    for data in datas:
        print(f'{data[0]} {data[1]}\t\t{data[3]}\t\t{data[2]}')

def Credentials(conn):
    print("Credential Check")
    c = conn.cursor()
    c.execute("SELECT user_name, password FROM members")
    datas = c.fetchall()
    print("USERNAME \tPASSWORD")
    print("---------\t--------")
    for data in datas:
        print(f'{data[0]}\t\t{data[1]}')
    input("press enter to exit")

def Register(conn):
    c = conn.cursor()
    firstname = input("What is your first name?:")
    lastname = input("What is your last name?:")
    email = input("What is your email?:")
    emailconfirm = input("Confirm your email:")

    if email != emailconfirm:
        print("Emails do not match!!")
        return

    username = input("Create Username:")
    privilege = 1 if username == "root" else 0
    password = maskpass.askpass(mask="")

    member_info = [(firstname, lastname, email, username, password, privilege)]
    c.executemany("INSERT INTO members VALUES (?,?,?,?,?,?)", member_info)
    print("Successfully Registered " + username)

def RRegister(conn):
    c = conn.cursor()
    firstname = input("What is your first name?:")
    lastname = input("What is your last name?:")
    email = input("What is your email?:")
    emailconfirm = input("Confirm your email:")

    if email != emailconfirm:
        print("Emails do not match!!")
        return

    username = input("Create Username:")
    privilege = 1 if username == "root" else 0
    password = maskpass.askpass(mask="")
    print("0 = non root, 1 = root")
    privilege = input("Priveledge (0 or 1)")

    member_info = [(firstname, lastname, email, username, password, privilege)]
    c.executemany("INSERT INTO members VALUES (?,?,?,?,?,?)", member_info)
    print("Successfully Registered " + username)

def Login():
    username = input("Username:")
    password = maskpass.askpass(mask="")
    hostname = socket.gethostname()
    IPAddr = socket.gethostbyname(hostname)

    conn = connect_to_db()
    c = conn.cursor()

    statement = f"SELECT user_name from members WHERE user_name = ? AND password = ?;"
    c.execute(statement, (username, password))
    if not c.fetchone():
        print("Login failed")
        disconnect_from_db(conn)
        exit()

    print("Welcome " + username)
    print("Your Computer Name is: " + hostname)
    print("Your Computer local IP Address is: " + IPAddr)

    RPcheck = f"SELECT user_name FROM members WHERE user_name = ? AND privilege = '1'"
    c.execute(RPcheck, (username,))
    if not c.fetchone():
        print("You are not admin")
        disconnect_from_db(conn)
        exit()

    menu = {'1': Roster, '2': Credentials, '3': RRegister, '7': "Exit"}
    while True:
        for entry, action in menu.items():
            print(entry, action.__name__ if callable(action) else action)
        selection = input("Please Select:")
        if selection in menu:
            if callable(menu[selection]):
                menu[selection](conn)
            else:
                break
        else:
            print("Unknown Option Selected!")
    disconnect_from_db(conn)