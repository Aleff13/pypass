from services.user import User
from services.password import Password
import PySimpleGUI as sg

class Pypass:

    def __init__(self) -> None:
        self.password = ""
        self.username = ""
        self.isLogged = False
        pass

    def isUserLogged(self) -> bool:
        return self.isLogged

    def login(self) -> bool:
        connection = User(self.username, self.password)
        connection.initDB()
        isLogged = connection.login()

        return isLogged

    def logout(self) -> bool:
        isLogged = False

        return isLogged

    def create_login_window(self):
            layout = [
                [sg.Text('Username:'), sg.Input(key='-USERNAME-')],
                [sg.Text('Password:'), sg.Input(key='-PASSWORD-', password_char='*')],
                [sg.Text('Confirm password:'), sg.Input(key='-CPASSWORD-', password_char='*')],
                [sg.Button('Login'), sg.Button('Cancel')]
            ]

            window = sg.Window('Login', layout)

            while True:
                event, values = window.read()

                if event == sg.WINDOW_CLOSED or event == 'Cancel':
                    break

                if event == 'Login':
                    self.username = values['-USERNAME-']
                    self.password = values['-PASSWORD-']
                    cpassword = values['-CPASSWORD-']

                    if (self.password != cpassword):
                        sg.popup('Login failed. Please try again.')

                    # Add your login logic here
                    if self.login():
                        sg.popup('Login successful!') 
                        self.isLogged = True
                        break
                    else:
                        sg.popup('Login failed. Please try again.')

            window.close()

    def create_select_option(self):
        layout = [
            [sg.Text('Select Operation:')],
            [sg.Combo(['Create', 'GetOne', 'GetAll', 'UpdateOne', 'RemoveOne'], key='-OPERATION-', enable_events=True)],
            [sg.Text('Title:'), sg.Input(key='-TITLE-')],
            [sg.Text('Email/Username:'), sg.Input(key='-USERNAME-')],
            [sg.Text('Password:'), sg.Input(key='-PASSWORD-', password_char='*')],
            [sg.Button('Execute'), sg.Button('Cancel')],
        ]

        window = sg.Window('Options', layout)
        svcSenha = Password()

        while True:
            event, values = window.read()

            if event == sg.WINDOW_CLOSED or event == 'Cancel':
                break

            if event == 'Execute':
                operation = values['-OPERATION-']
                title = values['-TITLE-']
                username = values['-USERNAME-']
                password = values['-PASSWORD-']

                if operation == 'Create':
                    sg.popup(f"Create operation selected. Username: {username}, Password: {password}")
                    svcSenha.createPassword(title, username, password)

                elif operation == 'GetOne':
                    value = svcSenha.getPassword(title)  
                    sg.popup(f"GetOne operation selected. Title: {value[0]} Username: {value[1]}, Password: {value[2]}")

                elif operation == 'GetAll':
                    values = svcSenha.getAllPasswords()
                    formatedValues = ""
                    for value in values:
                        formatedValues = formatedValues + "Title: {}, Email: {} e Senha: {}".format(value[0], value[1], value[2]) + "\n"
                    
                    sg.popup(f"{formatedValues}")
                elif operation == 'UpdateOne':
                    pass
                elif operation == 'RemoveOne':
                    svcSenha.deletePassword(title)
                    sg.popup(f"Password {title} removed")

        window.close()

init = Pypass()
init.create_login_window()

if init.isUserLogged() == True:
    init.create_select_option()
