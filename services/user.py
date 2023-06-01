import sqlite3
from services.hash import Hash
from services.crypt import Crypt
from services.password import Password

class User:

    dbUserPath = 'db/users.db'

    def __init__(self, name, password):
        self.name = name
        self.password = password

    def initDB(self):
        # Create a database and open the database.
        # If the database already exists just opens the database
        conn = sqlite3.connect(self.dbUserPath)
        c = conn.cursor()
        # Create a users table if the table does not exists
        c.execute('''CREATE TABLE IF NOT EXISTS users(username TEXT, pass TEXT)''')

        c.execute('''SELECT * FROM users''')
        rows = c.fetchall()

        if(rows == []):
            self.createUser()
            svcDbPass = Password()
            svcCrypt = Crypt()
            svcCrypt.generateKeys()
            svcDbPass.initDB()

        # commit changes and close database connect
        conn.commit()
        conn.close()

    def login(self) -> bool:
        conn = sqlite3.connect(self.dbUserPath)
        c = conn.cursor()
        c.execute('SELECT * FROM users WHERE (username == (?))', (self.name,))
        rows = c.fetchall()

        if(rows == []):
            return False
        
        DBHash = rows[0][1]
        return Hash.checkHash(DBHash, self.password)

    def createUser(self):
        conn = sqlite3.connect(self.dbUserPath)
        c = conn.cursor()

        hash = Hash.Encrypt(self.password)

        c.execute('INSERT INTO users(username, pass) VALUES (?, ?)', (self.name, hash))
        conn.commit()
        conn.close()

    def getUser(self) -> list:
        conn = sqlite3.connect(self.dbUserPath)
        c = conn.cursor()
        c.execute('select * from users')
        rows = c.fetchall()

        if(rows == []):
            return []
        
        user = [rows[0][0], rows[0][1]] 

        return user

    def showUser(self):
        conn = sqlite3.connect(self.dbUserPath)
        c = conn.cursor()
        c.execute('select * from users')
        rows = c.fetchall()

        for row in rows:
            print(row)
