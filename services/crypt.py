import rsa 

class Crypt:
    '''This class provides some methods to work with cryptography, like generate keys, encrypt and decrypt values'''

    def __init__(self) -> None:
        pass

    def generateKeys(self, path='keys/') -> bool:
        publicKey, privateKey = rsa.newkeys(1024)
        with open('{}publicKey.pem'.format(path), 'wb') as p:
            p.write(publicKey.save_pkcs1('PEM'))
        with open('{}privateKey.pem'.format(path), 'wb') as p:
            p.write(privateKey.save_pkcs1('PEM'))

        return True

    def loadKeys(self, path='keys/'):
        with open('{}publicKey.pem'.format(path), 'rb') as p:
            publicKey = rsa.PublicKey.load_pkcs1(p.read())
        with open('{}privateKey.pem'.format(path), 'rb') as p:
            privateKey = rsa.PrivateKey.load_pkcs1(p.read())

        return privateKey, publicKey

    def encrypt(self, message: str, publicKey) -> bytes:
        encMessage = rsa.encrypt(message.encode(), publicKey) 
        return encMessage

    def decrypt(self, encMessage: str, publicKey) -> str:
        decMessage = rsa.decrypt(encMessage, publicKey).decode() 

        return decMessage
