import sqlite3
import encript

class DBConn:

    def __init__(self, name, password):
        self.name = name
        self.password = password

    def initDB(self):
        # Create a database and open the database.
        # If the database already exists just opens the database
        conn = sqlite3.connect('users.db')
        c = conn.cursor()
        # Create a users table if the table does not exists
        c.execute('''CREATE TABLE IF NOT EXISTS users(username TEXT, pass TEXT)''')
        # commit changes and close database connect
        conn.commit()
        conn.close()

    def login(self):
        conn = sqlite3.connect('users.db')
        c = conn.cursor()
        svcEncript = encript.Crypt()
        c.execute('SELECT * FROM users WHERE (username == (?))', (self.name,))
        rows = c.fetchall()

        if(rows == []):
            print('EROU')
            return False
        
        DBHash = rows[0][1]
        return svcEncript.checkHash(DBHash, self.password)

    def createUser(self):
        conn = sqlite3.connect('users.db')
        c = conn.cursor()
        svcEncript = encript.Crypt()
        hash = svcEncript.Encrypt(self.password)
        c.execute('INSERT INTO users(username, pass) VALUES (?, ?)', (self.name, hash))
        conn.commit()
        conn.close()

    def showUsers(self):
        conn = sqlite3.connect('users.db')
        c = conn.cursor()
        c.execute('select * from users')
        rows = c.fetchall()

        for row in rows:
            print(row)

#password = str(input('Digite a senha que deseja utilizar: '))
#con = DBConn('admin', password)
# con.initDB()
# con.createUser()
#con.login()
#con.showUsers()