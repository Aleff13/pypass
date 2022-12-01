import rsa 

class criptografySVC:
    '''This service provides a serie of criptografy service like generate keys, ecnript and decript'''

    def __init__(self) -> None:
        pass

    def generateKeys(self):
        publicKey, privateKey = rsa.newkeys(1024)
        with open('publicKey.pem', 'wb') as p:
            p.write(publicKey.save_pkcs1('PEM'))
        with open('privateKey.pem', 'wb') as p:
            p.write(privateKey.save_pkcs1('PEM'))

    def loadKeys(self):
        with open('publicKey.pem', 'rb') as p:
            publicKey = rsa.PublicKey.load_pkcs1(p.read())
        with open('privateKey.pem', 'rb') as p:
            privateKey = rsa.PrivateKey.load_pkcs1(p.read())

        return privateKey, publicKey

    # def encrypt(self, message: str, key):
    #     return rsa.encrypt(message.encode('ascii'), key)

    # def decrypt(self, ciphertext, key):
    #     try:
    #         return rsa.decrypt(ciphertext, key).decode('ascii')
    #     except:
    #         return False

    def encrypt(self, message: str, publicKey) -> str:
        encMessage = rsa.encrypt(message.encode(), publicKey) 
        return encMessage

    def decrypt(self, encMessage: str, privateKey) -> str:
        decMessage = rsa.decrypt(encMessage, privateKey).decode() 

        return decMessage
