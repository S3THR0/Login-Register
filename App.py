import sqlite3
import maskpass
import socket
from module import *
import pyfiglet

def main():
    #Text in alligator font
    out = pyfiglet.figlet_format("S3THR0", font="alligator")
    print(out)

    #connect to database
    conn = connect_to_db()

    menu = {
        'L': Login,
        'R': Register,
        'exit': exit
    }

    for key, value in menu.items():
        print(f'[{key}]', value.__name__ if callable(value) else value)

    selection = input("Please Select:")
    if selection in menu:
        if callable(menu[selection]):
            menu[selection](conn)
        else:
            exit()
    else:
        print("Unknown Option Selected!")

    #commit command/save our progress
    disconnect_from_db(conn)

if __name__ == "__main__":
    main()