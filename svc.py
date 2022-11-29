import sqlite3
import encript

class DBSVC:

    def __init__(self, teste):
        self.teste = teste

    def initDB(self):
        # Create a database and open the database.
        # If the database already exists just opens the database
        conn = sqlite3.connect('passwords.db')
        c = conn.cursor()
        # Create a users table if the table does not exists
        c.execute('''CREATE TABLE IF NOT EXISTS passwords(title TEXT, email, TEXT, pass TEXT)''')
        # commit changes and close database connect
        conn.commit()
        conn.close()

    def createPass(self, title, email, password):
        encryptSVC = encript.Crypt()
        hash = encryptSVC.Encrypt(password)
        conn = sqlite3.connect('passwords.db')
        c = conn.cursor()
        c.execute('INSERT INTO passwords(title, email, pass) VALUES (?, ?, ?)', (title, email, hash))
        conn.commit()
        conn.close()

    def getPassword(self, title):
        conn = sqlite3.connect('passwords.db')
        c = conn.cursor()
        c.execute('SELECT * FROM passwords WHERE (title == (?))', (title,))
        rows = c.fetchall()

        for row in rows:
            print(row)

    def showPassword(self):
        conn = sqlite3.connect('passwords.db')
        c = conn.cursor()
        c.execute('SELECT * FROM passwords')
        rows = c.fetchall()

        for row in rows:
            print(row)       

# con = DBSVC('teste')

# #con.createUser()
# con.initDB()
# #con.createPass('teste', '123123')
# con.showPassword()