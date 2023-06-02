import unittest
from services.crypt import Crypt

mockKeyPath = 'tests/mocks/'

class HashTestClass(unittest.TestCase):

    def test_assertCan_a_GenerateKeys(self):
        service = Crypt()
        isKeysGenerated = service.generateKeys(mockKeyPath)

        self.assertTrue(isKeysGenerated)

    def test_assertCan_b_LoadKeys(self):
        service = Crypt()
        public, private = service.loadKeys(mockKeyPath)

        self.assertIsNotNone(public)
        self.assertIsNotNone(private)

    def test_assertCan_c_EncryptMessage(self):
        service = Crypt()
        public, private = service.loadKeys(mockKeyPath)

        message = 'hello'
        encryptMsg = service.encrypt(message, public)
        self.assertIsInstance(encryptMsg, bytes)

    def test_assertCan_d_DecryptMessage(self):
        service = Crypt()
        public, private = service.loadKeys(mockKeyPath)

        message = 'hello'
        encryptedMsg = service.encrypt(message, public)
        decryptMessage = service.decrypt(encryptedMsg, public)

        self.assertIsInstance(decryptMessage, str)

if __name__ == "__main__":
    unittest.main()