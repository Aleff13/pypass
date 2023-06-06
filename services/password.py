import sqlite3
from services.crypt import Crypt
from utils.colors import bcolors

class Password:

    ''' This class has services to work with the password db'''

    dbPasswordsPath = 'db/passwords.db'

    def __init__(self) -> None:
        return

    def initDB(self):
        conn = sqlite3.connect(self.dbPasswordsPath)
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS password(title TEXT PRIMARY KEY, email, TEXT, pass TEXT)''')

        conn.commit()
        conn.close()

    def createPassword(self, title: str, email: str, password: str):

        if (title == '' or email == '' or password == ''):
            print(bcolors.WARNING+ "Informe todos os valores para criar uma senha"+bcolors.ENDC)
            return

        conn = sqlite3.connect(self.dbPasswordsPath)
        c = conn.cursor()

        crypt = Crypt()
        pubKey, privateKey = crypt.loadKeys()
        cryptPass = crypt.encrypt(password, pubKey)

        try:

            c.execute('INSERT INTO password(title, email, pass) VALUES (?, ?, ?)', (title, email, cryptPass))
            conn.commit()
            conn.close()
            print(bcolors.OKGREEN+ "Senha para {} adicionada com sucesso".format(title)+bcolors.ENDC)
        except:
            print(bcolors.WARNING+ "Um erro ocorreu ao salvar a senha"+bcolors.ENDC)


    def getPassword(self, title: str):
        conn = sqlite3.connect(self.dbPasswordsPath)
        c = conn.cursor()

        c.execute('SELECT title, email, pass FROM password WHERE (title == (?))', (title,))
        rows = c.fetchall()

        crypt = Crypt()
        pubKey, privateKey = crypt.loadKeys()
        
        for row in rows:
            password = row[2]
            decPassword = crypt.decrypt(password, pubKey)
            print("Title: {}, Email: {} e Senha: {}".format(row[0], row[1], decPassword))

            password = [row[0], row[1], decPassword]

        return password
    
    def getAllPasswords(self):
        conn = sqlite3.connect(self.dbPasswordsPath)
        c = conn.cursor()

        c.execute('SELECT * FROM password')

        rows = c.fetchall()

        crypt = Crypt()
        pubKey, privateKey = crypt.loadKeys()

        decriptedPasswords = []

        for row in rows:
            password = row[3]
            decPassword = crypt.decrypt(password, pubKey)
            decriptedPasswords.append([row[0], row[1], decPassword])

            print("Title: {}, Email: {} e Senha: {}".format(row[0], row[1], decPassword))
        
        return decriptedPasswords


    
    def deletePassword(self, title: str):
        conn = sqlite3.connect(self.dbPasswordsPath)
        c = conn.cursor()

        try:
            c.execute('DELETE FROM password WHERE (title == (?))', (title,))

            conn.commit()
            conn.close()
            print(bcolors.OKGREEN+ "Senha de {} deletada com sucesso".format(title)+bcolors.ENDC)
        except:
            print(bcolors.WARNING+ "Um erro ocorreu"+bcolors.ENDC)
