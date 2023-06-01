import bcrypt

class Hash:

    def encodeString(value) -> bytes :
        return value.encode()

    def encrypt(password: str) -> bytes:
        if (type(password) != str):
            password = str(password)

        encodedPassword = Hash.encodeString(password)

        hashed = bcrypt.hashpw(encodedPassword, bcrypt.gensalt(14))
        return hashed
    
    def checkHash(hash: bytes, password: str) -> bool:
        if (type(password) != str):
            password = str(password)

        if (type(hash) != bytes):
            raise Exception("Hash provided can't be different of bytes")
        
        encodedPassword = Hash.encodeString(password)

        if bcrypt.checkpw(encodedPassword, hash):
            return True
        else:
            return False