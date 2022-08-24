import sqlite3

#connect to database
conn = sqlite3.connect("projectx.db")
        #sqlite3.connect(":memory:") for temp
#create cursor
c = conn.cursor()
#create table
c.execute("""CREATE TABLE members(
        first_name text,
        last_name text,
        email text NOT NULL UNIQUE,
        user_name text NOT NULL UNIQUE,
        password text
    )""")

#5 datatypes, NULL, INTEGER, REAL, TEXT, BLOB
"""
NULL - DOESNT EXIST
INTEGER - WHOLE NUMBERS
REAL - DECIMAL NUMBERS
TEXT - TEXT
BLOB - IMAGES, MP3 ETC
"""

#commit command/save our progress
conn.commit()
#close connection
conn.close()

print("Created database Successfully")
k=input("hit enter to exit:")