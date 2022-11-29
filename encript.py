import bcrypt
import hashlib

class Crypt:

    def __init__(self, password: str = ''):
        self.password = password

    def Encrypt(self, password):
        encodedPassword = self.encodeString(password)

        hashed = bcrypt.hashpw(encodedPassword, bcrypt.gensalt(14))
        return hashed
    
    def checkHash(self, hash, password) -> bool:
        encodedPassword = self.encodeString(password)

        if bcrypt.checkpw(encodedPassword, hash):
            return True
        else:
            return False   

    def encodeString(self, value):
        return value.encode()
        
# password = str(input("Digite sua senha: "))

# encript = Crypt()
# hash = encript.Encrypt(password)
# password = str(input("Digite sua senha: "))

# check = encript.checkHash(hash, password)

# print(check)
