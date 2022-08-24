import sqlite3

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
    statement = f"SELECT user_name from members WHERE user_name = '{username}';"
    c.execute(statement)
    if statement == False:
        print("Sorry, this username is not avaliable")
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