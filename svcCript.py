import rsa 

class criptografySVC:
    '''This service provides a serie of criptografy service like generate keys, ecnript and decript'''

    def __init__(self) -> None:
        pass

    def generateKeys(self):
        publicKey, privateKey = rsa.newkeys(1024)
        with open('keys/publcKey.pem', 'wb') as p:
            p.write(publicKey.save_pkcs1('PEM'))
        with open('keys/privateKey.pem', 'wb') as p:
            p.write(privateKey.save_pkcs1('PEM'))

    def loadKeys(self):
        with open('keys/publcKey.pem', 'rb') as p:
            publicKey = rsa.PublicKey.load_pkcs1(p.read())
        with open('keys/privateKey.pem', 'rb') as p:
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

# con = DBConn('admin', "235711")

svc = criptografySVC()
svc.generateKeys()
# # svc.setKeys()
# user = con.getUser()

# keys = [user[2], user[3]]

# print(keys)

# message = "senha 123123"

# #encriptar com a chave publica
# encMessage = svc.encrypt(message, keys[0])

# print("original string: ", message) 
# print("encrypted string: ", encMessage) 

# #descriptografar com a privateKey e a encMessage
# decMessage = svc.decrypt(encMessage, keys[1])
  
# print("decrypted string: ", decMessage) 