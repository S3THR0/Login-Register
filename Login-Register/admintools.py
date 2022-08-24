import sqlite3

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
    print(email)
    emailconfirm = input("Confirm your email:")

    if (email == emailconfirm):
        username = input("Create Username:")
        password = input("Enter Password:")
        member_info = [
                        (firstname, lastname, email, username, password)
                    ]

        c.executemany("INSERT INTO members VALUES (?,?,?,?,?)", member_info)
        print("Successfully Registered " + username)
    else:
        print("Please review email!!")





        #commit command/save our progress
    conn.commit()
    #close connection
    conn.close()
