import sqlite3

# create a new database
conn = sqlite3.connect('Library_database.db')

# Create a cursor object to allow to execute SQL commands
cursor = conn.cursor()

# -------------------------------------- BOOKS TABLE -------------------------------------- #
# Create a SQL Table
sql_command = '''
    CREATE TABLE IF NOT EXISTS Books (
        BookId INTEGER PRIMARY KEY AUTOINCREMENT,
        Title TEXT,
        Author TEXT
    )'''
cursor.execute(sql_command)
# Commit the changes to the database
conn.commit()

# -------------------------------------- BOOK MEMBERS TABLE -------------------------------------- #
# Create a SQL Table
sql_command = '''
    CREATE TABLE IF NOT EXISTS BookMember (
        BookId INTEGER PRIMARY KEY AUTOINCREMENT,
        MemberID INT
    )'''
cursor.execute(sql_command)
# Commit the changes to the database
conn.commit()

# -------------------------------------- MEMBERS TABLE -------------------------------------- #
# Create a SQL Table
sql_command = '''
    CREATE TABLE IF NOT EXISTS Members (
        BookId INTEGER PRIMARY KEY AUTOINCREMENT,
        MemberID INT
    )'''
cursor.execute(sql_command)
# Commit the changes to the database
conn.commit()
