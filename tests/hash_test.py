import unittest
from services.hash import Hash

class HashTestClass(unittest.TestCase):

    def test_assertEncodeString(self):
        password = '235711'

        encodedString = Hash.encodeString(password)

        self.assertIsInstance(encodedString, bytes)
    
    def test_encrypt(self):
        hash = Hash.encrypt('235711')

        self.assertIsNotNone(hash)
        self.assertIsInstance(hash, bytes)
    
    def test_encryptNumber(self):
        hash = Hash.encrypt(235711)

        self.assertIsNotNone(hash)
        self.assertIsInstance(hash, bytes)

    def test_checkHashIsTrue(self):
        password = '235711'

        hash = Hash.encrypt(password)
        isCorrectPassword = Hash.checkHash(hash, password)

        self.assertTrue(isCorrectPassword)

    def test_checkHashIsFalse(self):
        password = '235711'

        hash = Hash.encrypt(password)
        isInvalidPassword = Hash.checkHash(hash, '123123')

        self.assertFalse(isInvalidPassword)

if __name__ == "__main__":
    unittest.main()