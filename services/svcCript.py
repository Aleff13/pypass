import rsa 

class criptografySVC:
    '''This service provides a serie of criptografy service like generate keys, ecnript and decript'''

    def __init__(self) -> None:
        pass

    def generateKeys(self):
        publicKey, privateKey = rsa.newkeys(1024)
        with open('keys/publicKey.pem', 'wb') as p:
            p.write(publicKey.save_pkcs1('PEM'))
        with open('keys/privateKey.pem', 'wb') as p:
            p.write(privateKey.save_pkcs1('PEM'))

    def loadKeys(self):
        with open('keys/publicKey.pem', 'rb') as p:
            publicKey = rsa.PublicKey.load_pkcs1(p.read())
        with open('keys/privateKey.pem', 'rb') as p:
            privateKey = rsa.PrivateKey.load_pkcs1(p.read())

        return privateKey, publicKey

    def encrypt(self, message: str, publicKey) -> str:
        encMessage = rsa.encrypt(message.encode(), publicKey) 
        return encMessage

    def decrypt(self, encMessage: str, privateKey) -> str:
        decMessage = rsa.decrypt(encMessage, privateKey).decode() 

        return decMessage
