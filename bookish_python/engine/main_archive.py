import sqlite3

# create a new database
conn = sqlite3.connect('temp_database.db')

# Create a cursor to allow to execute SQL commands
cursor = conn.cursor()

# Create a SQL Table
sql_command = '''
    CREATE TABLE IF NOT EXISTS contacts (
        Id INTEGER PRIMARY KEY AUTOINCREMENT,
        Firstname TEXT,
        Lastname TEXT,
        Email TEXT
    )'''
cursor.execute(sql_command)
# Commit the changes to the database
conn.commit()

# insert data into the table, cursor object is used to control sql
insert_data = """
    INSERT INTO contacts
    (Firstname, Lastname, Email)
    VALUES (
        'David',
        'Attenborough',
        'dattenborough@example.com'
    )
"""
cursor.execute(insert_data)
# Commit the changes to the database
conn.commit()

select_data = 'SELECT * FROM contacts'
cursor.execute(select_data)
row = cursor.fetchone()
print(row)

users = [
    {'Firstname': 'Jane', 'Lastname': 'Goodall', 'Email': 'jgoodall@example.com'},
    {'Firstname': 'Rachel', 'Lastname': 'Carson', 'Email': 'rcarson@example.com'},
    {'Firstname': 'Barry', 'Lastname': 'Bishop', 'Email': 'bbishop@example.com'},
    {'Firstname': 'Edward', 'Lastname': 'J.Laurent', 'Email': 'ejlaurent@example.com'}
    ]

for user in users:
    insert_data = f"""
    INSERT INTO contacts 
    (Firstname, Lastname, Email) 
    VALUES (
        '{user['Firstname']}',
        '{user['Lastname']}',
        '{user['Email']}'
    )
    """
    cursor.execute(insert_data)
    conn.commit()

select_data = 'SELECT * FROM contacts'
cursor.execute(select_data)
rows = cursor.fetchall()

for row in rows:
    print(row)

# for this example code, this line prevents the table from having five names added on every iteration
delete_table = 'DROP TABLE contacts'
cursor.execute(delete_table)

# close the database at the end of the script
conn.close()


def createDatabases(self):
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


def createDatabaseOld(self):
    # create a new database
    conn = sqlite3.connect('Library_database.db')

    # Create a cursor object to allow to execute SQL commands
    cursor = conn.cursor()

    if len(self.fields) == 3:
        # Create a SQL Table
        sql_command = f'''
            CREATE TABLE IF NOT EXISTS {self.name} (
                {self.fields[0]} {self.types[0]},
                {self.fields[1]} {self.types[1]},
                {self.fields[2]} {self.types[2]}
            ) '''
    elif len(self.fields) == 2:
        # Create a SQL Table
        sql_command = f'''
            CREATE TABLE IF NOT EXISTS {self.name} (
                {self.fields[0]} {self.types[0]},
                {self.fields[2]} {self.types[2]}
            ) '''

    cursor.execute(sql_command)
    # Commit the changes to the database
    conn.commit()
    conn.close()