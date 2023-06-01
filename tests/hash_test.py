import unittest
from services.hash import Hash

class HashTestClass(unittest.TestCase):
    def testEncrypt(self):
        hashedPass = Hash.Encrypt("235711")
        self.assertIsNotNone(hashedPass)

if __name__ == "__main__":
    unittest.main()