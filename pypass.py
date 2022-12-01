from userDB import DBConn
from svcPassDB import DBSVC
import getpass
from colors import bcolors

class Pypass:

    def __init__(self, username, password) -> None:
        self.username = username
        self.password = password

    def getUser(self):
        user = [self.username, self.password]

        return user
    
    def isLogged(self) -> bool:
        connection = DBConn(self.username, self.password)
        connection.initDB()
        isLogged = connection.login()

        return isLogged

    def getOption(self) -> int:
        option = int(input('1- Criar nova senha, 2 - Buscar senha, 3 - Mostrar todas as senhas, 4 - sair: '))
        
        return option

    def printCollumn(self):
        print (bcolors.OKBLUE+'-------------------------------------'+bcolors.ENDC)

print (bcolors.OKBLUE+'-------------------------------------'+bcolors.ENDC)

username = str(input('Digite o nome de usuario: '))
password = str(getpass.getpass('Digite a senha de usuario: '))

init = Pypass(username, password)

isLogged = init.isLogged()

if(isLogged == True):
    
    svcSenha = DBSVC()
    while(isLogged == True):
        optionSelected = init.getOption()
        init.printCollumn()

        if(optionSelected == 1):
            title = str(input('Digite o titulo da senha: '))
            email = str(input('Digite o email: '))
            senha = str(getpass.getpass('Digite a senha: '))
            init.printCollumn()

            svcSenha.createPass(title, email, senha)
            
            init.printCollumn()

        if(optionSelected == 2):
            title = str(input('Digite o titulo da senha: '))
            init.printCollumn()

            svcSenha.getPassword(title)

            init.printCollumn()

        if(optionSelected == 3):
            svcSenha.getAllPasswords()

            init.printCollumn()

        if(optionSelected == 4):
            isLogged = False

            init.printCollumn()
