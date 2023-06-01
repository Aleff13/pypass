from services.user import User
from services.password import Password
import getpass
from utils.colors import bcolors

class Pypass:

    def __init__(self, username, password, confirmPassword) -> None:
        self.username = username
        self.password = password
        self.confirmPassword = confirmPassword

    def getUser(self):
        user = self.username

        return user
    
    def assertPasswords(self)-> bool:
        coincide = False
        if (self.confirmPassword == self.password):
            coincide = True 
        
        return coincide

    def isLogged(self) -> bool:
        if not self.assertPasswords():
            print("As senhas não coincidem")
            return False

        connection = User(self.username, self.password)
        connection.initDB()
        isLogged = connection.login()

        return isLogged

    def getOption(self) -> int:
        option = int(input('1- Criar nova senha, 2 - Buscar senha, 3 - Mostrar todas as senhas, 4 - Deletar uma senha, 5 - sair: '))
        
        return option

    def printCollumn(self):
        print (bcolors.OKBLUE+'-------------------------------------'+bcolors.ENDC)

print (bcolors.OKBLUE+'-------------------------------------'+bcolors.ENDC)

username = str(input('Digite o nome de usuario: '))
password = str(getpass.getpass('Digite a senha de usuario: '))
confirmPassword = str(getpass.getpass('Confirme a senha de usuario: '))

init = Pypass(username, password, confirmPassword)

isLogged = init.isLogged()
loggedUser = init.getUser()
svcSenha = Password()

if(isLogged == True):
    print('Você está logado como {}'.format(loggedUser))
    
    while(isLogged == True):
        optionSelected = init.getOption()
        init.printCollumn()

        if(optionSelected == 1):
            title = str(input('Digite o titulo da senha: '))
            email = str(input('Digite o email: '))
            senha = str(getpass.getpass('Digite a senha: '))
            init.printCollumn()

            svcSenha.createPassword(title, email, senha)
            
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
            title = str(input('Digite o titulo da senha: '))
            init.printCollumn()
            
            svcSenha.deletePassword(title)
            init.printCollumn()

        if(optionSelected == 5):
            isLogged = False

            init.printCollumn()
