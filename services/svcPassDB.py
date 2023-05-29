import sqlite3
from services.svcCript import criptografySVC
from colors import bcolors

class DBSVC:

    def __init__(self) -> None:
        return

    def initDB(self):
        conn = sqlite3.connect('db/passwords.db')
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS passwords(title TEXT, email, TEXT, pass TEXT)''')

        conn.commit()
        conn.close()

    def createPass(self, title: str, email: str, password: str):

        if (title == '' or email == '' or password == ''):
            print(bcolors.WARNING+ "Informe todos os valores para criar uma senha"+bcolors.ENDC)
            return

        conn = sqlite3.connect('db/passwords.db')
        c = conn.cursor()

        crypt = criptografySVC()
        pubKey, privateKey = crypt.loadKeys()
        cryptPass = crypt.encrypt(password, pubKey)

        try:
            c.execute('INSERT INTO passwords(title, email, pass) VALUES (?, ?, ?)', (title, email, cryptPass))
            conn.commit()
            conn.close()
            print(bcolors.OKGREEN+ "Senha para {} adicionada com sucesso".format(title)+bcolors.ENDC)
        except:
            print(bcolors.WARNING+ "Um erro ocorreu"+bcolors.ENDC)

    def getPassword(self, title: str):
        conn = sqlite3.connect('db/passwords.db')
        c = conn.cursor()

        c.execute('SELECT title, email, pass FROM passwords WHERE (title == (?))', (title,))
        rows = c.fetchall()

        crypt = criptografySVC()
        pubKey, privateKey = crypt.loadKeys()

        for row in rows:
            password = row[2]
            decPassword = crypt.decrypt(password, pubKey)
            print("Title: {}, Email: {} e Senha: {}".format(row[0], row[1], decPassword))

    def getAllPasswords(self):
        conn = sqlite3.connect('db/passwords.db')
        c = conn.cursor()

        c.execute('SELECT * FROM passwords')
        rows = c.fetchall()

        crypt = criptografySVC()
        pubKey, privateKey = crypt.loadKeys()

        for row in rows:
            password = row[3]
            decPassword = crypt.decrypt(password, pubKey)

            print("Title: {}, Email: {} e Senha: {}".format(row[0], row[1], decPassword))
