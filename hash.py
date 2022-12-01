import bcrypt

class Hash:

    def __init__(self, password: str = ''):
        self.password = password

    def Encrypt(self, password: str):
        encodedPassword = self.encodeString(password)

        hashed = bcrypt.hashpw(encodedPassword, bcrypt.gensalt(14))
        return hashed
    
    def checkHash(self, hash, password: str) -> bool:
        encodedPassword = self.encodeString(password)

        if bcrypt.checkpw(encodedPassword, hash):
            return True
        else:
            return False   

    def encodeString(self, value):
        return value.encode()
