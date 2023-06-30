import sqlite3
from services.hash import Hash
from services.crypt import Crypt
from services.password import Password
from shared.constants import Constants

#todo create a repository
class User:
    ''' This class has services to work with the user db'''

    dbPath = Constants.DATABASEPATH.value

    def __init__(self, name, password):
        self.name = name
        self.password = password

    def initDB(self):
        # Create a database and open the database.
        # If the database already exists just opens the database
        conn = sqlite3.connect(self.dbPath)
        c = conn.cursor()
        # Create a user table if the table does not exists
        c.execute('''CREATE TABLE IF NOT EXISTS user(id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT UNIQUE, pass TEXT)''')

        c.execute('''SELECT * FROM user''')

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
        conn = sqlite3.connect(self.dbPath)
        c = conn.cursor()
        c.execute('SELECT * FROM user WHERE (username == (?))', (self.name,))

        rows = c.fetchall()

        if(rows == []):
            return False
        
        DBHash = rows[0][2]
        return Hash.checkHash(DBHash, self.password)

    def createUser(self):
        conn = sqlite3.connect(self.dbPath)
        c = conn.cursor()

        hash = Hash.encrypt(self.password)

        c.execute('INSERT INTO user(username, pass) VALUES (?, ?)', (self.name, hash))

        conn.commit()
        conn.close()

    #todo: change this method to get by username
    def getUser(self) -> list:
        conn = sqlite3.connect(self.dbPath)
        c = conn.cursor()
        c.execute('select * from user')

        rows = c.fetchall()

        if(rows == []):
            return []
        
        user = [rows[0][0], rows[0][1]] 

        return user

    def showUser(self):
        conn = sqlite3.connect(self.dbPath)
        c = conn.cursor()
        c.execute('select * from user')

        rows = c.fetchall()

        for row in rows:
            print(row)
