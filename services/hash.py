import bcrypt

class Hash:

    def encodeString(value):
        return value.encode()

    def Encrypt(password: str):
        encodedPassword = Hash.encodeString(password)

        hashed = bcrypt.hashpw(encodedPassword, bcrypt.gensalt(14))
        return hashed
    
    def checkHash(hash, password: str) -> bool:
        encodedPassword = Hash.encodeString(password)

        if bcrypt.checkpw(encodedPassword, hash):
            return True
        else:
            return False   