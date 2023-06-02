import unittest
from services.crypt import Crypt

mockKeyPath = 'tests/mocks/'

class HashTestClass(unittest.TestCase):

    def test_assertCanGenerateKeys(self):
        service = Crypt()
        isKeysGenerated = service.generateKeys(mockKeyPath)

        self.assertTrue(isKeysGenerated)

    def test_assertCanLoadKeys(self):
        service = Crypt()
        public, private = service.loadKeys(mockKeyPath)

        self.assertIsNotNone(public)
        self.assertIsNotNone(private)

    def test_assertCanEncryptMessage(self):
        service = Crypt()
        public, private = service.loadKeys(mockKeyPath)

        message = 'hello'
        encryptMsg = service.encrypt(message, public)
        self.assertIsInstance(encryptMsg, bytes)

    def test_assertCanDecryptMessage(self):
        service = Crypt()
        public, private = service.loadKeys(mockKeyPath)

        message = 'hello'
        encryptedMsg = service.encrypt(message, public)
        decryptMessage = service.decrypt(encryptedMsg, public)

        self.assertIsInstance(decryptMessage, str)

if __name__ == "__main__":
    unittest.main()