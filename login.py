import sqlite3
import socket
from admintools import *
#from roster import Roster
#from credentials import Credentials
#from register import Register

username = input("Username:")
password = input("Password:")
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
else:
    print("Welcome " + username)
    print("Your Computer Name is: " + hostname)
    print("Your Computer local IP Address is: " + IPAddr)

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
        Register()
    elif selection == '7':
        break
    else:
        print("Unknown Option Selected!")

conn.commit()
conn.close()
