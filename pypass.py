import conn
import svc
import getpass

print ('-------------------------------------')

username = str(input('Digite o nome de usuario: '))
password = str(getpass.getpass('Digite a senha de usuario: '))

conection = conn.DBConn(username, password)

isLogged = conection.login()

if(isLogged == True):
    svcSenha = svc.DBSVC('')
    while(isLogged == True):
        optionSelected = int(input('1- Criar nova senha, 2 - Buscar senha, 3 - Mostrar todas as senhas, 4 - sair: '))

        if(optionSelected == 1):
            title = str(input('Digite o titulo da senha: '))
            email = str(input('Digite o email: '))
            senha = str(getpass.getpass('Digete a senha: '))
            svcSenha.createPass(title, email, senha)

        if(optionSelected == 2):
            title = str(input('Digite o titulo da senha: '))
            svcSenha.getPassword(title)

        if(optionSelected == 3):
            svcSenha.showPassword()
        
        if(optionSelected == 4):
            isLogged = False

print ('-------------------------------------')
