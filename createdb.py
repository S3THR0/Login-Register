import sqlite3
import pyfiglet

def main():
    # Text in alligator font
    out = pyfiglet.figlet_format("S3THR0", font="alligator")
    print(out)

    # Connect to database
    conn = sqlite3.connect("projectx.db")

    # Create cursor
    c = conn.cursor()

    # Create table
    c.execute("""
        CREATE TABLE members(
            first_name text,
            last_name text,
            email text NOT NULL UNIQUE,
            user_name text NOT NULL UNIQUE,
            password text,
            privilege integer
        )
    """)

    # Commit command/save our progress
    conn.commit()

    # Close connection
    conn.close()

    print("Created database Successfully")
    input("Press enter to exit:")

if __name__ == "__main__":
    main()