import sqlite3
import maskpass
import socket
from module import *

#connect to database
conn = sqlite3.connect("projectx.db")
        #sqlite3.connect(":memory:") for temp
#create cursor
c = conn.cursor()

menu = """
['L']="Login"
['R']="Register"
['exit']="Exit"
"""
print(menu)

selection = input("Please Select:")
if selection =='L':
    Login()
elif selection == 'R':
    Register()
elif selection == 'exit':
    exit()
else:
    print("Unknown Option Selected!")

#commit command/save our progress
conn.commit()
#close connection
conn.close()

